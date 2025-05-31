#administra as rotas do site
from app import app, sqlalchemy
from flask import render_template, url_for, jsonify, request, flash, redirect
from sqlalchemy import func

from app.models import clientes
from app.forms import clienteForm
from app.forms import atendimentoForm

#rota/pagina inicial
@app.route('/')
def home_page():

    return render_template('index.html')

#rota/cadastro de clientes
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = clienteForm()

    print("Método:", request.method)  # Verifica se é POST
    print("Formulário válido?", form.validate_on_submit())  # Mostra se passou na validação
    print("Erros no formulário:", form.errors)  # Mostra os erros se houver

    if form.validate_on_submit():
        form.save() #executa função save
        flash('Cliente cadastrado com sucesso!', 'success') #mensagem caso tudo ocorra certo
        return redirect(url_for('home_page')) #redireciona para pagina inicial
    
    return render_template('cadastro_novo.html', form=form)

#rota/pesquisar clientes
@app.route('/pesquisar')
def pesquisar():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    
    dados = clientes.query.order_by()
    
    if pesquisa != '':
        dados = dados.filter(func.lower(clientes.nome).like(f'{pesquisa.lower()}%'))
    context = {'dados': dados.all()}
    

    return render_template('pesquisar.html', context=context)

@app.route('/atendimento', methods=['GET', 'POST'])
def atendimento():
    form = atendimentoForm()

    form.nome.choices = [(c.nome, c.nome) for c in clientes.query.all()]

    print("Método:", request.method)  # Verifica se é POST
    print("Formulário válido?", form.validate_on_submit())  # Mostra se passou na validação
    print("Erros no formulário:", form.errors)  # Mostra os erros se houver

    if form.validate_on_submit():
        form.save() #executa função save
        flash('Cliente cadastrado com sucesso!', 'success') #mensagem caso tudo ocorra certo
        
        return redirect(url_for('home_page')) #redireciona para pagina inicial
    
    return render_template('atendimento.html', form=form)