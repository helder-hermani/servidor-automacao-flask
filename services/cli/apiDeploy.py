import sys
import os
import shutil

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from dependencies.getservers import listaExistingServers
from services.config import server_settings

class Deploy:

    def __init__(self) -> None:
        self.diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.root = os.path.abspath(os.path.join(diretorio_atual, '..', '..', '..'))
        self.root_current = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
        self.config_atual = server_settings()
        self.servers = listaExistingServers()
        self.nome_server_atual = self.config_atual['serverName']
        self.dados_servidor_atual = self.servidor_atual()

    def lista_servidores(self):
        lista_destinos = []
        for server in self.servers:
            if (server['server_name'].strip() != self.config_atual['serverName'].strip()):
                lista_destinos.append(server["folder"])
        return lista_destinos
    
    def servidor_atual(self):
        for server in self.servers:
            if (server['server_name'].strip() == self.config_atual['serverName'].strip()):
                return server
        return None


    def listar_arquivos_e_pastas(self, diretorio):
        estrutura = []
        schema = []

        for root, dirs, files in os.walk(diretorio):
            estrutura.append({
                'pasta': root,
                'arquivos': files
            })

        for diretorio in estrutura:
            for arquivo in diretorio['arquivos']:
                path = f"{diretorio['pasta']}\{arquivo}"
                schema.append(path.replace('\\','\\\\'))

        return schema
        
        
    def deploy_arquivo(self, arquivo, lista_ignore):
        deploy = True
        if (arquivo.find('__pycache__') >= 0):
            return False
        if (arquivo.find('.git') >= 0):
            return False
        if (arquivo.find('.env') >= 0):
            return False
        if (arquivo.find('logs\\\\history') >= 0):
            return False
        if (arquivo.find('services\\\\logs\\\\requests.log') >= 0):
            return False
        for ignore in lista_ignore:
            ignore = ignore.replace('\\','\\\\')
            if (arquivo.find(ignore) >= 0):
                return False
        return deploy
    
    def make_backup(self,servidor_destino):
        diretorio_backup = f'{self.root}/deploybackup'
        shutil.rmtree(diretorio_backup)
        shutil.copytree(servidor_destino, diretorio_backup)

    
    def make_deploy(self, servidor_destino):
        schema = self.listar_arquivos_e_pastas(self.root_current)

        lista_ignore = []
        with open('.deployignore', 'r') as file_ignore:
            ignore_file_content = file_ignore.readlines()
            for linha in ignore_file_content:
                ignore = linha.strip()
                path = f'{self.root_current}\{ignore}'
                lista_ignore.append(path)

        for item in schema:
            deploy = self.deploy_arquivo(item,lista_ignore)
            if (deploy):
                item_formatado = item.replace('\\\\','\\')
                root_current_formatado = self.root_current.replace('\\','\\\\')
                destino = item_formatado.replace(self.dados_servidor_atual['folder'],servidor_destino)
                destino = item_formatado.replace(self.root_current,f'c:\\flask\\{servidor_destino}')
                os.makedirs(os.path.dirname(destino), exist_ok=True)
                shutil.copy(item_formatado,destino)

                

# -----------------------------------------------

appDeploy = Deploy()
appDeploy.make_backup('flask.prod.caixa')
appDeploy.make_deploy('flask.prod.caixa')