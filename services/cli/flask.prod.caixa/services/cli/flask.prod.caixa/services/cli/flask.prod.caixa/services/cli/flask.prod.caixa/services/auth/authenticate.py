import requests
from flask import session, url_for
from cryptography.fernet import Fernet
from services.auth.consultaLDAP import Ldap

def authenticate_user(app, user, password):
    ldap = Ldap(user, password)
    print('Passou na Ldap')
    if (ldap.success):
        app_key_encoded = app.secret_key.encode()
        cipher_suite = Fernet(app_key_encoded)
        crypt_token = cipher_suite.encrypt(app_key_encoded)
    
        dados_user = ldap.consultaMatricula(user)

        url = f'https://novoredevarejo.caixa/api/administrativo-free/funcionarios/avatar/{user}'
        get_user_avatar = requests.get(url, verify=False)
        if (get_user_avatar.status_code == 200):
            avatar_url = url
        else:
            avatar_url = url_for('static', filename='app/assets/img/perfil-sem-foto.png')

        token = crypt_token.decode()

        session['token'] = token
        session['avatar_url'] = avatar_url
        session['user_auth'] = dados_user

        user_auth = {
            'token': token,
            'dados_user':dados_user,
            'avatar_url': avatar_url
            }

        ldap.fechaConexao()
        return user_auth
    else:
        print('---------------------------------------------------')
        print('Erro na conexão Ldap')
        # ldap.fechaConexao()
        return None
    
def check_authentication(secret_key, token):
    cipher_suite = Fernet(secret_key)
    token_encoded = token.encode()
    auth_token = cipher_suite.decrypt(token_encoded)

    if (auth_token.decode() == secret_key):
        return True
    else:
        return False




