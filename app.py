from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector




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


    # ROTAS
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/msgindex', methods=['POST'])
    def msgindex():
        msgi = "Mensagem enviada com sucesso"
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
                msg = "Nome já cadastrado, tá tudo errado"
            else:
                email = request.form['email']
                telefone = request.form['telefone']
                pessoa = Pessoa(
                    nome_completo=nome_completo,
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