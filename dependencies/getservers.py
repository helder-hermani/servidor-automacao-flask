import os
import sys

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings

def listaServersConfig():
    server = server_settings()

    # Verificar demais servidores
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
    print(path)

    folders = [diretorio for diretorio in os.listdir(path) if os.path.isdir(os.path.join(path, diretorio))]

    lista_servers = []
    server_id = 0
    for servidor in folders:
        print(servidor)
        arquivo = f'{path}\\{servidor}\\.env'
        if os.path.exists(arquivo):
            # print(f"O arquivo {arquivo} existe no diretório '{servidor}'.")
            instancias = []
            with open(arquivo, 'r', encoding='utf-8') as arquivo_env:
                env = arquivo_env.readlines()

                isServer = False
                server_name = None
                version = None
                environment = None
                port_python = None
                port_conda = None

                for variavel in env:
                    if ((variavel.find('SERVER_NAME') >= 0)):
                        isServer = True
                        linha_split = variavel.split('=')
                        server_name = linha_split[1]
                    if ((variavel.find('VERSION') >= 0)):
                        isServer = True
                        linha_split = variavel.split('=')
                        version = linha_split[1]
                    if ((variavel.find('ENVIRONMENT') >= 0)):
                        isServer = True
                        linha_split = variavel.split('=')
                        environment = linha_split[1]
                    if ((variavel.find('PORT_PYTHON') >= 0)):
                        instancias.append('Python Padrão')
                        linha_split = variavel.split('=')
                        port_python = linha_split[1]
                    if ((variavel.find('PORT_CONDA') >= 0)):
                        instancias.append('Anaconda')
                        linha_split = variavel.split('=')
                        port_conda = linha_split[1]

                    if (server_name != None and version != None and environment != None):
                        isServer = True
                    
                if (isServer):
                    for instancia in instancias:
                        server_id = server_id + 1
                        if (instancia=='Python Padrão'):
                            port = port_python
                            domain = server['protocolo'] + '://' + server['ip'] + ':' + port
                        elif (instancia=='Anaconda'):
                            port = port_conda
                            domain = server['protocolo'] + '://' + server['ip'] + ':' + port

                        existing_server = {
                            'server_id': server_id,
                            'server_name': server_name,
                            'version': version,
                            'environment': environment,
                            'instance': instancia,
                            'port_python': port,
                            'domain': domain,
                            'ping_url': f'{domain}/api',
                            'folder': servidor
                        }
                        lista_servers.append(existing_server)
    
    return lista_servers

def listaExistingServers():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))

    folders = [diretorio for diretorio in os.listdir(path) if os.path.isdir(os.path.join(path, diretorio))]

    lista_servers = []
    for servidor in folders:
        # print(servidor)
        arquivo = f'{path}\\{servidor}\\.env'
        if os.path.exists(arquivo):
            # print(f"O arquivo {arquivo} existe no diretório '{servidor}'.")
            instancias = []
            with open(arquivo, 'r', encoding='utf-8') as arquivo_env:
                env = arquivo_env.readlines()

                isServer = False
                server_name = None
                version = None
                environment = None
                port_python = None
                port_conda = None

                for variavel in env:
                    if ((variavel.find('SERVER_NAME') >= 0)):
                        isServer = True
                        linha_split = variavel.split('=')
                        server_name = linha_split[1]
                    if ((variavel.find('VERSION') >= 0)):
                        isServer = True
                        linha_split = variavel.split('=')
                        version = linha_split[1]
                    if ((variavel.find('ENVIRONMENT') >= 0)):
                        isServer = True
                        linha_split = variavel.split('=')
                        environment = linha_split[1]
                    
                    if (server_name != None and version != None and environment != None):
                        isServer = True
                    
                if (isServer):
                        existing_server = {
                            'server_name': server_name,
                            'version': version,
                            'folder': servidor
                        }
                        lista_servers.append(existing_server)
    
    return lista_servers