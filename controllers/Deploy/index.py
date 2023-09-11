import sys
import os
from flask import render_template

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from dependencies.getservers import listaExistingServers
from services.config import server_settings
from services.cli.apiDeploy import Deploy

def show():
    apiDeploy = Deploy()
    servers = apiDeploy.lista_servidores()
    servidor_atual = apiDeploy.dados_servidor_atual['folder']
    ignore_file = apiDeploy.getDeployIgnore()

    print('=======================================================================')
    print(servers)
    print(servidor_atual)
    print(ignore_file)
    print('=======================================================================')
    # apiDeploy.make_deploy('flask.prod.caixa')
    return render_template('deploy/deploy.html.jinja',servers=servers,servidor_atual=servidor_atual, ignore_file=ignore_file)

def makeBackup(servidor_destino):
    try:
        apiDeploy = Deploy()
        apiDeploy.make_backup(servidor_destino)
        return {'status': f'Backup de {servidor_destino} realizado com sucesso!'}
    except Exception as err:
        return str(err)
    
def makeDeploy(servidor_destino, useIgnore):
    try:
        if (int(useIgnore) == 0):
            useIgnore = False
        else:
            useIgnore = True

        print('=======================================================================')
        print('=======================================================================')
        print('=======================================================================')
        print(useIgnore)
        print('=======================================================================')
        print('=======================================================================')
        print('=======================================================================')
        apiDeploy = Deploy()
        apiDeploy.make_deploy(servidor_destino, useIgnore)
        return {'status': f'Deploy para {servidor_destino} concluído com sucesso!'}
    except Exception as err:
        return str(err)