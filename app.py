from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import smtplib
from email.message import EmailMessage

def create_app():

    app = Flask(__name__)
    app.secret_key = "abax"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/gbxp'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:A532DD-DGgBD3EA4eCd5h6hDa-f6EBd4@viaduct.proxy.rlwy.net:30787/railway'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cdh3dcE2edd33A66f61a1fH6db31HdGc@monorail.proxy.rlwy.net:51466/railway'
    db = SQLAlchemy(app)

    # Conexão com o email:
    EMAIL_ADDRESS = 'gamebarretosexperience@gmail.com'
    # Use a senha de aplicativo gerada no lugar da sua senha normal
    EMAIL_PASSWORD = 'mpho hcrl ermm ixxo'


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

                message = EmailMessage()
                message['Subject'] = 'Bem-vindo à Game Barretos Experience!'
                message['From'] = 'gamebarretosexperience@gmail.com'
                message['To'] = email
                message.set_content(f"""
Olá {nome}.
Se você está recebendo este e-mail, é porque acabou de se cadastrar na Game Barretos Experience! 
Nós da equipe GBXP estamos muito animados por ter você conosco. A GBXP é um evento anual que celebra o mundo dos jogos, trazendo experiências únicas, competições emocionantes e uma atmosfera vibrante para todos os apaixonados por games. Estamos ansiosos para recebê-lo(a) no evento e proporcionar momentos inesquecíveis.
                                    
Se por acaso você não se cadastrou ou não reconhece este registro, por favor, nos avise imediatamente para que possamos investigar qualquer atividade não autorizada.

Fique ligado(a) para mais informações sobre a GBXP, incluindo horários, programação de atividades e detalhes sobre o local do evento. Seja muito bem-vindo(a) à Game Barretos Experience! Mal podemos esperar para viver essa experiência incrível juntos.
                                    
Atenciosamente, Equipe GBXP.""")

                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        smtp.send_message(message)
                        print("E-mail enviado com sucesso!")
                except Exception as e:
                    print(f"Erro ao enviar e-mail: {str(e)}")


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