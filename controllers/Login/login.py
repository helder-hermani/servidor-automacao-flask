import random
import json
from flask import abort, render_template, redirect
from controllers.Login.classes.Login import obj_login

def handle_login(app, request):
    auth = obj_login.autentica_usuario(app, request)

    print('Dados da autenticação:')
    print(auth)

    if (auth != None):
        if (request.path.find('/api') >= 0):
            return json.dumps({'auth_data':auth}, ensure_ascii=False).encode('utf-8')
        else:
            print(auth)
            return redirect('/')
            # return redirect('/home')
    else:
        if (request.path.find('/api') >= 0):
            return abort(403)
        else:
            user = request.form.get('user')
            handle_login_otp(user)
            return render_template('/index/index.html.jinja',erroAuth = True, loginOTP=True, user=user)
            return "Falha na autenticação"

def handle_login_otp(user):
    codigo_otp = ''
    email = f'{user}@corp.caixa.gov.br'
    for i in range(5):
        codigo_otp = codigo_otp + chr(random.randint(48,122))
    print(email)
    print(codigo_otp)


def handle_logout():
    return redirect('/')