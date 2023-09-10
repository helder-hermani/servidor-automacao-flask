import os
import sys
import shutil

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..','..'))
sys.path.append(diretorio_pai)
from dependencies.getservers import listaExistingServers
from dependencies.interface import p
from services.config import server_settings

def getServers():
    # print('Diretório pai: ' + diretorio_pai)
    servidor_atual = server_settings()
    nome_server_atual = servidor_atual['serverName']
    servers = listaExistingServers()

    # print(servidor_atual)
    # print(servers)

    print('')
    print('----------------------------------------------------------------------------------')
    print('------------------------------------ DEPLOY --------------------------------------')
    print('----------------------------------------------------------------------------------')
    print('')
    print('Servidores disponíveis:')
    lista_destinos = []
    for server in servers:
        if (server['server_name'].strip() != servidor_atual['serverName'].strip()):
            lista_destinos.append(server["folder"])
            p(f'--> {server["folder"]}','primary')

    print('')
    servidor_destino = input('Informe o servidor de DESTINO: ')
    print('')

    if (servidor_destino not in lista_destinos):
        p('Servidor informado não existe.','danger')
        sys.exit()

    p(f'ATENÇÃO: Ao confirmar o deploy, os arquivos no servidor {servidor_destino} serão SOBRESCRITOS pelos arquivos do servidor {nome_server_atual} (este). Após confirmar, o processo será IRREVERSÍVEL.', 'warning')
    continuar = input('Deseja continuar (s/n)?')

    if (continuar.upper() != 'S'):
        print('Processo abortado.','danger')
    else:
        p(f'Enviar ambiente virtual? Utilize esta funcionalidade se tiver instalado novas bibliotecas.')
        deploy_venv = input('Deseja enviar ambiente virtual (s/n)?')

        if (deploy_venv.upper() == 'S'):
            print('Ambiente virtual será enviado.')
            venv = True
        else:
            print('Ambiente virtual NÃO será enviado.')
            venv = False

        # ---------------------------------------------------------------------------------------------------
        # INICIA BACKUP
        # ---------------------------------------------------------------------------------------------------

        p('--------------------------------------------','warning')
        p('-------------- Iniciando Deploy ------------','warning')
        p('--------------------------------------------','warning')
        print('')
        
        p(f'--> Preparando backup de {servidor_destino}','primary')
        root = os.path.abspath(os.path.join(diretorio_atual, '..', '..','..','..'))
        diretorio_backup = f'{root}/deploybackup'

        try:
            shutil.rmtree(diretorio_backup)
            print(f"Diretório de backup preparado com sucesso.")
        except OSError as e:
            print(f"Erro ao excluir o diretório '{diretorio_backup}': {e}")

        p(f'--> Iniciando backup de {servidor_destino}','primary')
        diretorio_destino = f'{root}/{servidor_destino}'
        folders_destino = [diretorio for diretorio in os.listdir(diretorio_pai) if os.path.isdir(os.path.join(diretorio_pai, diretorio))]

        for folder in folders_destino:
            if (folder != '.venv' and folder != 'static' and folder != '.git'):
                print(f'Iniciando backup de {folder}')
                try:
                    if (folder != '.venv' and folder != 'static'):
                        shutil.copytree(f'{diretorio_destino}/{folder}', f'{diretorio_backup}/{folder}')
                        print(f"Backup realizado com sucesso.")
                        # print(f"O diretório '{servidor_destino}' e todo o seu conteúdo foram copiados para '{diretorio_backup}' com sucesso.")
                except OSError as e:
                    print(f"Erro ao copiar o diretório: {e}")

        # Backup de static, exceto o subdiretório app (bibliotecas estáticas)
        if os.path.exists(f'{diretorio_destino}/static'):
            folders_destino = [diretorio for diretorio in os.listdir(f'{diretorio_destino}/static') if os.path.isdir(os.path.join(f'{diretorio_destino}/static', diretorio))]

            for folder in folders_destino:
                print(f'Iniciando backup de {folder}')
                try:
                    if (folder != 'app'):
                        shutil.copytree(f'{diretorio_destino}/static/{folder}', f'{diretorio_backup}/static/{folder}')
                        print(f"Backup realizado com sucesso.")
                except OSError as e:
                    print(f"Erro ao copiar o diretório: {e}")

        arquivos = os.listdir(diretorio_destino)
        arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(diretorio_destino, arquivo))]
        for arquivo in arquivos:
            if (arquivo != '.env'):
                print(f'Iniciando backup de {diretorio_destino}/arquivo')
                try:
                    shutil.copy(f'{diretorio_destino}/{arquivo}', f'{diretorio_backup}/{arquivo}')
                    print(f"Backup realizado com sucesso.")
                except IOError as e:
                    print(f"Erro ao copiar o arquivo: {e}")

        p('------------------------------','success')
        p('Backup concluido com sucesso!','success')
        p('------------------------------','success')


        # ---------------------------------------------------------------------------------------------------
        # INICIA DEPLOY
        # ---------------------------------------------------------------------------------------------------
        print('')
        p('--> Mapeando estrutura de arquivos','primary')
        print('')


        folders = [diretorio for diretorio in os.listdir(diretorio_pai) if os.path.isdir(os.path.join(diretorio_pai, diretorio))]

        for folder in folders:
            print(f'Iniciando deploy de {folder}')
            if (folder != '.git' and folder != 'static'):
                if (folder == '.venv' and venv == True):
                    try:
                        if os.path.exists(f'{diretorio_destino}/{folder}'):
                            shutil.rmtree(f'{diretorio_destino}/{folder}')
                        shutil.copytree(f'{diretorio_pai}/{folder}', f'{diretorio_destino}/{folder}')
                        print(f"Deploy de {folder} realizado com sucesso.")
                    except OSError as e:
                        print(f"Erro ao copiar o diretório: {e}")
                if (folder != 'static' and folder != '.git' and folder != '.venv'):
                    try:
                        if os.path.exists(f'{diretorio_destino}/{folder}'):
                            shutil.rmtree(f'{diretorio_destino}/{folder}')
                        shutil.copytree(f'{diretorio_pai}/{folder}', f'{diretorio_destino}/{folder}')
                        print(f"Deploy de {folder} realizado com sucesso.")
                    except OSError as e:
                        print(f"Erro ao copiar o diretório: {e}")

        # Backup de static, exceto o subdiretório app (bibliotecas estáticas)
        folders = [diretorio for diretorio in os.listdir(f'{diretorio_pai}/static') if os.path.isdir(os.path.join(f'{diretorio_pai}/static', diretorio))]

        for folder in folders:
            print(f'Iniciando backup de {folder}')
            try:
                if (folder != 'app'):
                    if os.path.exists(f'{diretorio_destino}/static/{folder}'):
                        shutil.rmtree(f'{diretorio_destino}/static/{folder}')
                    shutil.copytree(f'{diretorio_pai}/static/{folder}', f'{diretorio_destino}/static/{folder}')
                    print(f"Deploy de {folder} realizado com sucesso.")
            except OSError as e:
                print(f"Erro ao copiar o diretório: {e}")

        arquivos = os.listdir(diretorio_pai)
        arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(diretorio_pai, arquivo))]
        for arquivo in arquivos:
            if (arquivo != '.env'):
                print(f'Iniciando backup de {diretorio_pai}/{arquivo}')
                try:
                    if os.path.exists(f'{diretorio_destino}/{arquivo}'):
                        os.remove(f'{diretorio_destino}/{arquivo}')
                    shutil.copy(f'{diretorio_pai}/{arquivo}', f'{diretorio_destino}/{arquivo}')
                    print(f"Backup realizado com sucesso.")
                except IOError as e:
                    print(f"Erro ao copiar o arquivo: {e}")

        p('------------------------------','success')
        p('Deploy concluido com sucesso!','success')
        p('------------------------------','success')

        # arquivos = os.listdir(diretorio_pai)

        # # Filtre para listar apenas os arquivos (excluindo subdiretórios)
        # arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(diretorio_pai, arquivo))]

        # # Imprima a lista de arquivos
        # for arquivo in arquivos:
        #     print(arquivo)


getServers()