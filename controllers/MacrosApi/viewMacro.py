import sys
import os
import markdown
from flask import render_template

import dependencies.loadinfofile as loadFile

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings

def index(request):
    readme = request.args.get('readme')
    filepath = request.args.get('filepath')
    print(readme)
    # readme = f'{os.path.dirname(os.path.abspath(__file__))}\\readme.md'
    info = loadFile.loadInfo(readme)
    infoRequest = loadFile.getInfoRequest(readme)
    htmlSnippet = loadFile.generateHtmlSnippet(readme)
    cssSnippet = loadFile.generateCssSnippet(readme)
    jsSnippet = loadFile.generateJsSnippet(readme)
    controllerSnippet = loadFile.generateControllerSnippet(readme)
    rotaLaravelSnippet = loadFile.generateRotaLaravelSnippet(readme)

    server = server_settings()
    dominio = server['dominio']
    rotaApi = f'{dominio}{infoRequest["rotaApi"]}'

    conteudo_html = markdown.markdown(info)

    return render_template('webMacroApi/macro.html.jinja',filepath=filepath, rotaApi=rotaApi, infoRequest=infoRequest, info=conteudo_html, htmlSnippet=htmlSnippet, cssSnippet=cssSnippet, jsSnippet=jsSnippet, controllerSnippet=controllerSnippet, rotaLaravelSnippet=rotaLaravelSnippet)