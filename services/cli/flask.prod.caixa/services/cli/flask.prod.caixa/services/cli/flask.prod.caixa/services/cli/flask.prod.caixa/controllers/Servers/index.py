import os
import sys
from flask import render_template

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings
from dependencies.getservers import listaServersConfig

def index():
    server = server_settings()
    lista_servers = listaServersConfig()
    
    return render_template('/home/index.html.jinja',server=server, lista_servers=lista_servers)