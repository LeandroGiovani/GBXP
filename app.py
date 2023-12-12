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

    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USERNAME'] = 'gbxp2023@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'GameBarretosExperience2023##'
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USE_SSL'] = False

    # teste1 
    # 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 
        

    app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'  # Altere para o servidor SMTP correto do SendGrid
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'teste2'  # Seu usuário de API
    app.config['MAIL_PASSWORD'] = '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'  # Sua chave de API do SendGrid
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
# 
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
                msg = "Cadastro feito com sucesso"
                bbox = True

        else:
            msg = "" 
            bbox = False
            rbox = False 

        return render_template('form.html', msg=msg, bbox=bbox, rbox=rbox)
    


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
            mensagemteste1['From'] = 'gbxp2023@gmail.com'
            mensagemteste1['To'] = 'arth4asy@gmail.com'
            password = 'GameBarretosExperience2023##' 
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
        sender_email = "gbxp2023@gmail.com"
        recipient_email = "arth4asy@gmail.com"
        email_subject = "GBXP está feliz com você!"
        email_content = "Olá, você acabou de se cadastrar no Game Barretos Experience. Te esperamos lá!"

        msg = Message(subject=email_subject, sender=sender_email, recipients=[recipient_email])
        msg.body = email_content

        try:
            mail.send(msg)
            print("E-mail enviado com sucesso!")
            return render_template('index.html')  # Renderiza o template após enviar o e-mail
        except Exception as e:
            print(f"Erro ao enviar e-mail: {str(e)}")
            return str(e), 500  # Retorna o erro como resposta HTTP 500 Internal Server Error

    @app.route('/teste2')
    def send_mail():
        mansagem = Message('Assunto do E-mail', sender='gbxp2023@gmail.com', recipients=['arth4asy@gmail.com'])
        mansagem.body = 'Conteúdo do E-mail'
        mail.send(mansagem)
        return 'E-mail enviado com sucesso!'


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