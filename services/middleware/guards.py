from flask import session, request
from services.auth.authenticate import check_authentication

open_routes = ['/favicon.ico', '/login', '/dologin', '/api/dologin', '/api', '/macro', '/macroapi', '/logout']

def middleware_guards(secret_key, token):
    def authenticate(secret_key, token):
        return check_authentication(secret_key, token)
    
    possui_acesso = authenticate(secret_key, token)

    if (possui_acesso):
        permission = True
    else:
        permission = False

    return permission

def is_open_route():
    print('----------------------')
    print(request.root_url)
    if (request.path in open_routes or request.path.startswith('/static/') or request.path=='/'):
        return True
    else:
        for route in open_routes:
            full_request_route = f'{request.root_url}{request.path}'
            if (full_request_route.find(f'{request.root_url}{route}') == 0):
            # if (full_request_route.find(route) == 0):
                return True
            
        return False
