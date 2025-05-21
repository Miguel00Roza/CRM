#administra as rotas do site
from app import app
from flask import render_template, url_for, jsonify
import random

#rota/pagina inicial
@app.route('/')
def home_page():
    context = {
        'usuario': 'Miguel',
        'idade': 15,
        'cargo': 'estudante'
    }

    return render_template('index.html', context=context)

#rota secundaria, está foi criada como teste
@app.route('/new')
def nova():
    return 'teste de pagina'