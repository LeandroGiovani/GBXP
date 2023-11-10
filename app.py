from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os
import smtplib
from email.message import EmailMessage
from flask_mail import Mail, Message


def create_app():



    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    # CONEXÃO COM BANCO DE DADOS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/gbxp'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://root:5e5i_123@localhost/gbxp'
    db = SQLAlchemy(app)

    # VARIÁVEIS DO BANCO
    class Pessoa(db.Model):

        __tablename__ = "cadastro"
        #  coloque o nome da tabela

        idcadastro = db.Column(db.Integer, primary_key=True)
        nome_completo = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(100),nullable=False)
        telefone = db.Column(db.String(45), nullable=False)

        # def __repr__(self):
        #     return f'<Pessoa {self.nome_completo + self.telefone}>'
        # print(__repr__)]

    # parte do email :)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Substitua pelo servidor SMTP correto
    app.config['MAIL_PORT'] = 465  # Substitua pela porta correta
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'gamebarretosexperience@gmail.com'
    app.config['MAIL_PASSWORD'] = 'gbxp2023'

    mail = Mail(app)


    # ROTAS
    @app.route('/')
    def index():
        # q = request.args.get('q')
    
        # if q:
        #     pessoas = Pessoa.query.filter((Pessoa.nome_completo.like(f"%{q}%")) | (Pessoa.cpf.like(f"%{q}%"))).all()
        # else:
        #     pessoas = Pessoa.query.all()
        return render_template('index.html')
    @app.route('/form', methods=['GET', 'POST'])
    def form():
        inc_msg = "" 
        msg = inc_msg
        if request.method == 'POST':
            nome_completo = request.form['nome_completo']

            # Verificar se o nome já existe no banco de dados
            pessoa_existente = Pessoa.query.filter_by(nome_completo=nome_completo).first()

            if pessoa_existente:
                # Se o nome já existe, preencha os outros campos do formulário
                email = pessoa_existente.email
                telefone = pessoa_existente.telefone
                msg = "Nome já cadastrado, seus dados foram atualizados"
            else:
                email = request.form['email']
                telefone = request.form['telefone']
                pessoa = Pessoa(
                    nome_completo=nome_completo,
                    email=email,
                    telefone=telefone
                )
                db.session.add(pessoa)
                msg = inc_msg   

            db.session.commit()
            
        return render_template('form.html', msg=msg, inc_msg=inc_msg)  # Passar msg para o template


    @app.route('/send_message', methods=['GET','POST'])
    def send_message():
        if request.method == "POST":
            semail = request.form['email']
            subject = request.form['nome_completo']
            mensagem = request.form['message']

            message = Message(subject,sender="gamebarretosexperience@gmail.com",recipients=[semail])
            message.body = mensagem
            mail.send(message)

            success = "Message sent"

        return render_template("result.html", success=success)


    @app.route('/loja')
    def loja():

        return render_template('loja.html')
    
    @app.route('/carrinho')
    def car():
        return render_template('carrinho.html')
      
    # tentar privar isso depois
    @app.route('/verificar_nome', methods=['GET'])
    def verificar_nome():
        nome = request.args.get('nome')  # Obtenha o nome da consulta de URL
        pessoa = Pessoa.query.filter_by(nome_completo=nome).first()

        if pessoa:
            # Se o nome já existir, retorne seus detalhes em JSON
            return {
                'nome_completo': pessoa.nome_completo,
                'email': pessoa.email,
                'telefone': pessoa.telefone
            }
        else:
            # Se o nome não existir, retorne um objeto JSON vazio
            return {}
    return app

if __name__ == '__main__':
    create_app().run(debug=True)