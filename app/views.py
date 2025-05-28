#administra as rotas do site
from app import app, db
from flask import render_template, url_for, request, flash, redirect

from app.models import clientes
from app.forms import clienteForm

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
    dados = clientes.query.all()
    context = {'dados': dados}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'buscar': pesquisa})
    

    return render_template('pesquisar.html', context=context)