#administra as rotas do site
from app import app
from flask import render_template, url_for, jsonify

#rota/pagina inicial
@app.route('/')
def home_page():

    return render_template('index.html')

#rota secundaria, está foi criada como teste
@app.route('/cadastro')
def cadastro():
    
    return render_template('cadastro.html')