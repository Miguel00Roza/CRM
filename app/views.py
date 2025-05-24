#administra as rotas do site
from app import app, db
from flask import render_template, url_for, jsonify, request

from app.models import clientes

#rota/pagina inicial
@app.route('/')
def home_page():

    return render_template('index.html')

#rota/cadastro de clientes
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        telefone = request.form['telefone']
        email = request.form['email']
        mensagem = request.form['texto']

        Clientes = clientes(
            nome=nome,
            idade=idade,
            telefone=telefone,
            email=email,
            comentario=mensagem
        )

        db.session.add(Clientes)
        db.session.commit()
    

    return render_template('cadastro.html')

#rota/pesquisar clientes
@app.route('/pesquisar')
def pesquisar():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'buscar': pesquisa})
    

    return render_template('pesquisar.html', context=context)