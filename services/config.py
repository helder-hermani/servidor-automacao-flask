import sys
import os
from dotenv import load_dotenv
from services.network.getip import get_local_ip

# class ServerInfo:
#     def __init__(self) -> None:
#         self.serverInfo = server_settings()


def verifica_ambiente_virtual():
    if 'CONDA_DEFAULT_ENV' in os.environ:
        ambiente_virtual = os.environ['CONDA_DEFAULT_ENV']
        if ambiente_virtual == 'base':
            ambiente_txt = "O script está sendo executado no ambiente virtual base do Conda."
            ambiente_anaconda = True
        else:
            ambiente_txt = f"O script está sendo executado em um ambiente virtual do Conda: {ambiente_virtual}"
            ambiente_anaconda = True
    else:
        ambiente_txt = "O script está sendo executado no ambiente virtual padrão do Python."
        ambiente_anaconda = False

    if 'CONDA_PREFIX' in os.environ:
        caminho_python = os.path.join(os.environ['CONDA_PREFIX'], 'bin', 'python')
        versao_txt = f'Python versão Anaconda: {sys.version}'
        # try:
        #     resultado = os.popen(f'{caminho_python} --version').read()
        #     versao = resultado.strip().split()[-1]
        #     versao_txt = f'Python versão no ambiente virtual: {versao}'
        # except Exception as e:
        #     versao_txt = f'Erro ao verificar a versão do Python: {str(e)}'
    else:
        versao_txt = f'Versão python padrão: {sys.version}'

    return{
        'ambiente_txt': ambiente_txt,
        'ambiente_anaconda': ambiente_anaconda,
        'versao_txt': versao_txt
    }


def server_settings():
    load_dotenv()
    serverName = os.environ['SERVER_NAME']
    versao = os.environ['VERSION']
    ambiente = os.environ['ENVIRONMENT']
    user_authenticate = os.environ['USER_AUTHENTICATE'] != "False"
    
    protocolo = 'http'
    current_ip = get_local_ip()

    if (user_authenticate):
        master = None
    else:
        master = "MASTER"

    interpretador =  verifica_ambiente_virtual()

    if (interpretador['ambiente_anaconda']):
        port = os.environ['PORT_CONDA']
    else:
        port = os.environ['PORT_PYTHON']

    return {
            'serverName': serverName,
            'versao': versao,
            'ambiente': ambiente,
            'protocolo': protocolo,
            'porta':port,
            'dominio': f'{protocolo}://{current_ip}:{port}',
            'ip': current_ip,
            'master': master,
            'ambiente_txt': interpretador['ambiente_txt'],
            'versao_txt': interpretador['versao_txt'],
            'isAnaconda': interpretador['ambiente_anaconda']
        }