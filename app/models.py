# Banco de dados
from app import db
from datetime import datetime

# classe clientes / modelo de tabela no banco de dados
class clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_de_envio = db.Column(db.DateTime, default = datetime.now())
    nome = db.Column(db.String, nullable=True)
    idade = db.Column(db.Integer, nullable=True)
    telefone = db.Column(db.String)
    email = db.Column(db.String, nullable=True)
    comentario = db.Column(db.String)

