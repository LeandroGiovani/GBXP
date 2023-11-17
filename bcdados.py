from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
# from app import create_app


app = Flask(__name__) # instancia o Flask
app.secret_key = "abax"
# CONEXÃO COM BANCO DE DADOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/gbxp'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://root:5e5i_123@localhost/gbxp'
db = SQLAlchemy(app)

# class Pessoa(db.Model):

#         __tablename__ = "clientes"

#         idclientes = db.Column(db.Integer, primary_key=True)
#         nome = db.Column(db.String(100))
#         email = db.Column(db.String(100))
#         telefone = db.Column(db.String(45))

class Mensagem(db.Model):

        __tablename__ = "mensagens"

        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(100))
        email = db.Column(db.String(100))
        mensagem = db.Column(db.String(45))

