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


# <div class="success">
#     <div class="success__icon">
#       <svg xmlns="http://www.w3.org/2000/svg" width="24" viewBox="0 0 24 24" height="24" fill="none"><path fill-rule="evenodd" fill="#393a37" d="m12 1c-6.075 0-11 4.925-11 11s4.925 11 11 11 11-4.925 11-11-4.925-11-11-11zm4.768 9.14c.0878-.1004.1546-.21726.1966-.34383.0419-.12657.0581-.26026.0477-.39319-.0105-.13293-.0475-.26242-.1087-.38085-.0613-.11844-.1456-.22342-.2481-.30879-.1024-.08536-.2209-.14938-.3484-.18828s-.2616-.0519-.3942-.03823c-.1327.01366-.2612.05372-.3782.1178-.1169.06409-.2198.15091-.3027.25537l-4.3 5.159-2.225-2.226c-.1886-.1822-.4412-.283-.7034-.2807s-.51301.1075-.69842.2929-.29058.4362-.29285.6984c-.00228.2622.09851.5148.28067.7034l3 3c.0983.0982.2159.1748.3454.2251.1295.0502.2681.0729.4069.0665.1387-.0063.2747-.0414.3991-.1032.1244-.0617.2347-.1487.3236-.2554z" clip-rule="evenodd"></path></svg>
#     </div>
#     <div class="success__title">lorem ipsum dolor sit amet</div>
#     <div class="success__close"><svg xmlns="http://www.w3.org/2000/svg" width="20" viewBox="0 0 20 20" height="20"><path fill="#393a37" d="m15.8333 5.34166-1.175-1.175-4.6583 4.65834-4.65833-4.65834-1.175 1.175 4.65833 4.65834-4.65833 4.6583 1.175 1.175 4.65833-4.6583 4.6583 4.6583 1.175-1.175-4.6583-4.6583z"></path></svg></div>
# </div>
# .success {
#   font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
#   width: 320px;
#   padding: 12px;
#   display: flex;
#   flex-direction: row;
#   align-items: center;
#   justify-content: start;
#   background: #84D65A;
#   border-radius: 8px;
#   box-shadow: 0px 0px 5px -3px #111;
# }

# .success__icon {
#   width: 20px;
#   height: 20px;
#   transform: translateY(-2px);
#   margin-right: 8px;
# }

# .success__icon path {
#   fill: #393A37;
# }

# .success__title {
#   font-weight: 500;
#   font-size: 14px;
#   color: #393A37;
# }

# .success__close {
#   width: 20px;
#   height: 20px;
#   cursor: pointer;
#   margin-left: auto;
# }

# .success__close path {
#   fill: #393A37;
# }
