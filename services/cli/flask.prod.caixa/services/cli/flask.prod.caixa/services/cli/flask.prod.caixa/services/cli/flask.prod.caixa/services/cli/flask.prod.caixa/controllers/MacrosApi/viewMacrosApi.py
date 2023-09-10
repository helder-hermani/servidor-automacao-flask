
import os
from flask import render_template

import dependencies.loadinfofile as infoFile

def index():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_macros_api = os.path.abspath(os.path.join(diretorio_atual, '..', '..', 'macros', 'Api'))

    macros_api = [diretorio for diretorio in os.listdir(diretorio_macros_api) if os.path.isdir(os.path.join(diretorio_macros_api, diretorio))]

    lista_macros = []
    for macro in macros_api:
        if (macro != '__pycache__'):
            path_macro = f'{str(diretorio_macros_api)}\{macro}'
            info = infoFile.getMacroInfo(path_macro)
            lista_macros.append(info)

    print(lista_macros)
    return render_template('webMacroApi/index.html.jinja', lista_macros=lista_macros)