from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import smtplib
import email.message
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask_mail import Mail, Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_app():

    app = Flask(__name__)
    app.secret_key = "abax"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/gbxp'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:A532DD-DGgBD3EA4eCd5h6hDa-f6EBd4@viaduct.proxy.rlwy.net:30787/railway'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cdh3dcE2edd33A66f61a1fH6db31HdGc@monorail.proxy.rlwy.net:51466/railway'
    db = SQLAlchemy(app)

    # VARIÁVEIS DO BANCO
    class Pessoa(db.Model):

        __tablename__ = "clientes"
        #  coloque o nome da tabela

        idclientes = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(100),nullable=False)
        telefone = db.Column(db.String(45), nullable=False)
        

    
    class Mensagem(db.Model):

        __tablename__ = "mensagem"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        memail = db.Column(db.String(100))
        # msg = db.Column(db.String(45)) - ultimo que deu certo
        msg = db.Column(db.String(200))

        # assunto = db.Column(db.String(45))

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'gamebarretosexperience@gmail.com'
    app.config['MAIL_PASSWORD'] = 'gbxp2023'        

    mail = Mail(app)
    
    # ROTAS
    @app.route('/')
    def index():
        noti = False

        return render_template('index.html', noti=noti)
    
    @app.route('/msgindex', methods=['POST'])
    def msgindex():

        name = request.form['name']
        memail = request.form['memail']
        msg = request.form['msg']

        mensagem = Mensagem(name=name, memail=memail, msg=msg)
        db.session.add(mensagem)
        db.session.commit()

        noti = True

        return render_template('index.html', noti=noti)
    
    @app.route('/form', methods=['GET', 'POST'])
    def form():
        bbox = False
        rbox = False

        if request.method == 'POST':
            email = request.form['email']
            pessoa_existente = Pessoa.query.filter_by(email=email).first()
    
            if pessoa_existente:
                msg = "Esse email já foi cadastrado"
                rbox = True
            else:
                nome = request.form['nome']
                telefone = request.form['telefone']
                pessoa = Pessoa(
                    nome=nome,
                    email=email,
                    telefone=telefone
                )
                db.session.add(pessoa)
                db.session.commit()
                mens = "Cadastro feito com sucesso"
                bbox = True

                mens = Message(sender='gamebarretosexperience@gmail.com', recipients=['arth4asy@gmail.com'])
                mens.body = f"Nome: {nome}\nE-mail: {email}"

                mail.send(mens)
                
        else:
            msg = "" 
            bbox = False
            rbox = False 
    
        return render_template('form.html', msg=msg, bbox=bbox, rbox=rbox, sucesso=True)



    @app.route('/loja')
    def loja():

        return render_template('loja.html')
    
    @app.route('/carrinho')
    def car():
        return render_template('carrinho.html')

    @app.route('/teste')
    def teste():
        def enviar_email():  
            corpo_email = """
            <p>Parágrafo1</p>
            <p>Parágrafo2</p>
            """ 

            mensagemteste1 = email.message.Message()
            mensagemteste1['Subject'] = "Assunto"
            mensagemteste1['From'] = 'gamebarretosexperience@gmail.com'
            mensagemteste1['To'] = 'arth4asy@gmail.com'
            password = 'gbxp2023' 
            mensagemteste1.add_header('oi', 'ola')
            mensagemteste1.set_payload(corpo_email )   

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(mensagemteste1['From'], password)
            s.sendmail(mensagemteste1['From'], [mensagemteste1['To']], mensagemteste1.as_string().encode('utf-8'))
            print('Email enviado')  


             # In[ ]:    


            enviar_email()

        return render_template('index.html')

    @app.route('/teste1')
    def teste1():
        SENDGRID_API_KEY = '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'  # Substitua pelo seu próprio SendGrid API Key

        # Configure as informações do e-mail
        sender_email = "gamebarretosexperience@gmail.com"
        recipient_email = "arth4asy@gmail.com"
        email_subject = "GBXP está feliz com você!"
        email_content = "Olá, você acabou de se cadastrar no Game Barretos Experience. Te esperamos lá!"

        message = Mail(
            from_email=sender_email,
            to_emails=recipient_email,
            subject=email_subject,
            plain_text_content=email_content
        )

        try:
            sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
            response = sg.send(message)
            print("E-mail enviado com sucesso!")
            print(f"Código de status: {response.status_code}")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {str(e)}")

        return render_template('index.html')

    @app.route('/teste2')
    def teste2():
        def enviar_email(destinatario, assunto, corpo):
            # Configurações do servidor SMTP do Gmail
            email_origem = 'gamebarretosexperience@gmail.com'
            senha = 'gbxp2023'
            smtp_server = 'smtp.gmail.com'
            smtp_porta = 587  # Porta para TLS

            # Criando a mensagem
            mensagem = MIMEMultipart()
            mensagem['From'] = email_origem
            mensagem['To'] = destinatario
            mensagem['Subject'] = assunto

            # Adicionando o corpo do e-mail
            mensagem.attach(MIMEText(corpo, 'plain'))

            # Criando uma conexão segura com o servidor SMTP
            try:
                server = smtplib.SMTP(smtp_server, smtp_porta)
                server.starttls()
                server.login(email_origem, senha)
                server.sendmail(email_origem, destinatario, mensagem.as_string())
                print('E-mail enviado com sucesso!')
            except Exception as e:
                print(f'Erro ao enviar e-mail: {e}')
            finally:
                server.quit()  # Fechar a conexão com o servidor SMTP

            # Exemplo de uso
            destinatario = 'arth4asy@gmail.com'
            assunto = 'Assunto do e-mail'
            corpo = 'Olá, este é um exemplo de e-mail enviado via Python.'

            enviar_email(destinatario, assunto, corpo)

        return render_template('index.html')


    # tentar privar isso depois
    @app.route('/verificar_nome', methods=['GET'])
    def verificar_nome():
        nomev = request.args.get('nome')  # Obtenha o nome da consulta de URL
        pessoa = Pessoa.query.filter_by(nome=nomev).first()

        if pessoa:
            # Se o nome já existir, retorne seus detalhes em JSON
            return {
                'nome_completo': pessoa.nome,
                'email': pessoa.email,
                'telefone': pessoa.telefone
            }
        else:
            # Se o nome não existir, retorne um objeto JSON vazio
            return {}
    return app

if __name__ == '__main__':
    create_app().run(debug=True)