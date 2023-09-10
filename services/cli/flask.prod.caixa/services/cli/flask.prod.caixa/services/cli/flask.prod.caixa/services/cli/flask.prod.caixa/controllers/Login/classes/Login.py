from services.auth.authenticate import authenticate_user

class Login:
    def __init__(self):
        pass

    def autentica_usuario(self, app, request):
        if (request.path.find('/api') >= 0):
            req = request.json
            user = req['user']
            password = req['password']
        else:
            user = request.form.get('user')
            password = request.form.get('password')

        print('Dados do login:')
        print(user)
        print(password)

        dados_user = authenticate_user(app,user,password)

        print('Retorno da autenticação:')
        print(dados_user)

        return dados_user

obj_login = Login()