#arquivo que inicia tudo
from app import app

#verifica se esse é o arquivo __main__, colocando a permissao de execução do programa só nele
if __name__ == '__main__':
    app.run(debug=True)

