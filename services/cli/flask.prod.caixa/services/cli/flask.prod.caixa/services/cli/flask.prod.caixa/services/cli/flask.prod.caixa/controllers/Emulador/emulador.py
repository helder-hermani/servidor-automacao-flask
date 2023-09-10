import sys
import os
from flask import Flask, render_template, session
import markdown
import random
import string

import dependencies.loadinfofileAut as infoFile

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_macros_aut = os.path.abspath(os.path.join(diretorio_atual, '..', '..', 'macros', 'Automacao'))

def showEmulador():
    server = server_settings()
    dominio = server['dominio']

    macros_aut = [diretorio for diretorio in os.listdir(diretorio_macros_aut) if os.path.isdir(os.path.join(diretorio_macros_aut, diretorio))]

    macrosRegistradas = []
    for macro in macros_aut:
        if (macro != '__pycache__'):
            path_macro = f'{str(diretorio_macros_aut)}\{macro}'
            info = infoFile.getMacroInfo(path_macro)
            macrosRegistradas.append(info['name'])

    if 'user_auth' in session:
        user = session['user_auth']['matricula']
    else:
        if (server['master'] != None):
            user = server['master']
        else:
            return render_template('config/access-denied.html.jinja')

    print('=======================================================================================')
    print(f'USUÁRIO: {user}')
    print('=======================================================================================')

    return render_template('emulador/index.html.jinja', macrosRegistradas=macrosRegistradas, dominio=dominio, user=user)

def getMacroInfo(macroName):
    path_macro = f"{str(diretorio_macros_aut)}\{macroName}"
    info = infoFile.loadInfo(f'{path_macro}\\readme.md')
    conteudo_html = markdown.markdown(info)
    return conteudo_html


def macroPlay(macroName):
    # Pega Rota
    path_macro = f'{str(diretorio_macros_aut)}\{macroName}'
    info = infoFile.getMacroInfo(path_macro)
    
    # Gera Id para a requisição
    length = 6
    caracteres = string.ascii_letters + string.digits
    reqId = ''.join(random.choice(caracteres) for _ in range(length))
    
    server = server_settings()
    dominio = server['dominio']
    rota = f'{dominio}{info["route"]}'

    return {
        'reqId':reqId.upper(),
        'name':info['name'],
        'route': rota
    }

