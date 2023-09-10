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

def showEmuladorExterno(macroName, user):
    server = server_settings()
    dominio = server['dominio']

    return render_template('emulador/externo.html.jinja', dominio=dominio, macro=macroName, user=user)