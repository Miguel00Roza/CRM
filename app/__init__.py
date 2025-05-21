#transforma a pasta em um modulo
#ainda não compreendi direito, pesquisar sobre no futuro
from flask import Flask

app = Flask(__name__)


from app.views import home_page