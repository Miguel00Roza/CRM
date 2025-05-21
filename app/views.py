from app import app
from flask import render_template, url_for, jsonify
import random

@app.route('/')
def home_page():
    context = {
        'usuario': 'Miguel',
        'idade': 15,
        'cargo': 'estudante'
    }

    return render_template('index.html', context=context)

@app.route('/new')
def nova():
    return 'teste de pagina'