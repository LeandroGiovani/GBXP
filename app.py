from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector




def create_app():

    app = Flask(__name__)
    app.secret_key = "abax"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/gbxp'
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
        msg = db.Column(db.String(45))
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
        inc_msg = "" 
        msg = inc_msg
        if request.method == 'POST':
            nome = request.form['nome']

            # Verificar se o nome já existe no banco de dados
            pessoa_existente = Pessoa.query.filter_by(nome=nome).first()

            if pessoa_existente:
                msg = "Nome já cadastrado, tá tudo errado"
            else:
                email = request.form['email']
                telefone = request.form['telefone']
                pessoa = Pessoa(
                    nome=nome,
                    email=email,
                    telefone=telefone
                )
                db.session.add(pessoa)
                msg = "Cadastro perfeitamente perfeito" 

            db.session.commit()
            
        return render_template('form.html', msg=msg, inc_msg=inc_msg)  # Passar msg para o template


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
