import os
from dotenv import load_dotenv
from services.network.getip import get_local_ip


def server_settings():
    load_dotenv()
    ambiente = os.environ['AMBIENTE']
    default_protocol = os.environ['DEFAULT_PROTOCOL']
    user_authenticate = os.environ['USER_MASTER'] == ""
    
    https = default_protocol == 'https'

    if (ambiente == 'PROD'):
        if (https):
            protocolo = 'https'
            port = os.environ['PORT_HTTPS_PROD']
        else:
            protocolo = 'http'
            port = os.environ['PORT_HTTP_PROD']
    elif (ambiente == 'DES'):
        if (https):
            protocolo = 'https'
            port = os.environ['PORT_HTTPS_DES']
        else:
            protocolo = 'http'
            port = os.environ['PORT_HTTP_DES']

    current_ip = get_local_ip()

    if (user_authenticate):
        master = None
    else:
        master = os.environ['USER_MASTER']

    return {
            'ambiente': ambiente,
            'protocolo': protocolo,
            'porta':port,
            'dominio': f'{protocolo}://{current_ip}:{port}',
            'ip': current_ip,
            'master': master
        }

    # SERVER = get_server()
    # return AppConfig.SERVER
