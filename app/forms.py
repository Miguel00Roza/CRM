from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, IntegerField, TextAreaField , SubmitField, SelectField
from wtforms.validators import DataRequired, Email

from app import db
from app.models import clientes
from app.models import atendimento

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


class atendimentoForm(FlaskForm):
    nome = SelectField('Nome', choices=[])
    situacao = SelectField('Situação',
    choices=[
        ('quente', 'quente'),
        ('morno', 'morno'),
        ('frio', 'frio'),
        ('fechou com outro', 'fechou com outro'),
        ('fechou com nós', 'fechou com nós'),
        ('desistiu', 'desistiu')
    ], validators=[DataRequired()])
    piscina = SelectField('modelo',
    choices=[
        ('passione spa', 'passione spa'),
        ('passione praia', 'passione praia'),
        ('piazza', 'piazza'),
        ('new fiori', 'new fiori'),
        ('veneza spa', 'veneza spa')
    ], validators=[DataRequired()])
    vendedor = StringField('Quem atendeu?', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        # salva os dados do cliente
        Atendimento = atendimento(
            nome=self.nome.data,
            situacao=self.situacao.data,
            piscina=self.piscina.data,
            vendedor=self.vendedor.data
        )
        # envia os dados para o banco de dados 
        db.session.add(Atendimento)
        db.session.commit()
    

