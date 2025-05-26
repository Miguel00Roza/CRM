from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, IntegerField, TextAreaField , SubmitField
from wtforms.validators import DataRequired, Email

from app import db
from app.models import clientes

# inputs e botão submit
class clienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    telefone = TelField('Telefone')
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    comentario = TextAreaField('Sobre o cliente')
    btnSubmit = SubmitField('Enviar')

    # Função save
    def save(self):
        # salva os dados do cliente
        Clientes = clientes(
            nome=self.nome.data,
            idade=self.idade.data,
            telefone=self.telefone.data,
            email=self.email.data,
            comentario=self.comentario.data
        )
        # envia os dados para o banco de dados 
        db.session.add(Clientes)
        db.session.commit()


