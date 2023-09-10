import os
import sys

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from services.cli.api import CliApi

def make(request):
    params = request.json
    nome = params['nome']
    titulo = params['titulo']
    desc = params['desc']
    metodo = params['metodo']
    args = params['args']

    appCli = CliApi()
    return appCli.makeMacroApi(nome, titulo, desc, metodo, args)

def delete(request):
    params = request.json
    nome = params['nome']
    metodo = params['metodo']
    
    appCli = CliApi()
    return appCli.deleteMacroApi(nome,metodo)