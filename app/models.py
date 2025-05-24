from app import db
from datetime import datetime

class clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_de_envio = db.Column(db.DateTime, default = datetime.now())
    nome = db.Column(db.String, nullable=True)
    idade = db.Column(db.Integer, nullable=True)
    telefone = db.Column(db.String, nullable=True)
    email = db.Column(db.String)
    comentario = db.Column(db.String)

