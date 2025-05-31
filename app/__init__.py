#transforma a pasta em um modulo
#ainda não compreendi direito, pesquisar sobre no futuro = Acho que esse arquivo é onde importamos as bibliotecas e distribuimos entre os arquivos
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '124G@#$@#EH@#$@6%#AN283*@_!MWIFU#@$&@#*EN9783!@#$*jmfj3*#l'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views import home_page
from app.models import clientes