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
   
    appCli = CliApi()
    return appCli.makeAutomacao(nome, titulo, desc)

def delete(request):
    params = request.json
    nome = params['nome']
    metodo = params['metodo']
    
    appCli = CliApi()
    return appCli.deleteMacroApi(nome,metodo)