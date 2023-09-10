=======================================
SOMENTE PELO GITBASH:
=======================================

1.) Criar ambiente virtual:
$ py -3 -m venv .venv

2.) Ativar o ambiente virtual
$ source .venv/Scripts/activate

3.) Instalar Flask no ambiente virtual:
python -m pip install flask -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa

4.) Criar o arquivo index.py:
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<p>Hello World</p>'

---------------------------------------------------------------------------------------------------
5.) Iniciar o servidor em localhost: $ flask --app index run

6.) Iniciar o servidor em um ip específico, na porta padrão (5000): flask --app index run --host=10.123.28.128

========================================================================================
7.) Iniciando servidor em endereço ip e porta específica:

7.1) usando o Waitress (RECOMENDÁVEL)

python -m pip install waitress -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
from waitress import serve
if __name__ == '__main__':
    app.debug = True
    serve(app, host=local_server_ip, port=5000)

-- Iniciar como python index.py
-- app.debug inicia o modo debugger (não rodar em ambiente de produção)
-- Iniciar como python index.py

---------------------------------------------------------------------------------------------------
7.2) Usando método nativo do Flask
if __name__ == '__main__':
    app.debug = True
    app.run(host=local_server_ip, port=7077)

-- Iniciar como python index.py

========================================================================================

8.) Utilizando o hot reload:

ATENÇÃO: NECESSÁRIO ATIVAR O app.debug = True

a.) Instalar o watchdog: $ python -m pip install watchdog -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa

b.) Importar as bilbiotecas:

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

c.) Implementar a inicialização:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    app.debug=ambienteDev
    serve(app, host=local_server_ip, port=7077)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

========================================================================================

9.) Função para pegar o ip local:
import socket

def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as e:
        print('Erro ao obter o endereço IP:', str(e))
    
    return None

========================================================================================
10.) autenticação pela Ldap

python -m pip install ldap3 -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa

11.) Roteiro:

a.) Acessar o ambiente virtual pelo GITBASH: $ source .venv/Scripts/activate
b.) Instalar as seguintes dependências:

    python -m pip install flask -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install waitress -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install watchdog -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install ldap3 -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install cryptography -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install flask-jwt -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install requests -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install markdown -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install flask_cors -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install pandas -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install openpyxl -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install colorama -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install Flask-Bootstrap -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install Flask-FontAwesome -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa
    python -m pip install python-dotenv -i http://binario.caixa:8081/repository/pypi-repo/simple --trusted-host binario.caixa

12.) Gerando certificado SSL autoassinado:
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 3650    

13.) Comandos do CLI
./cli.sh -m minhaApp42 "Primeira Aplicação" "Minha aplicação de teste" get user,password


