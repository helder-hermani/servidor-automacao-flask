import socket

def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as e:
        print('Erro ao obter o endereço IP:', str(e))
    
    return None