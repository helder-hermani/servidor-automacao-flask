# -*- coding: utf-8 -*-
import os
from flask import session, request, render_template, current_app
from waitress import serve
import sys
import ssl
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# import logging
# from logging.handlers import RotatingFileHandler

from cryptography.fernet import Fernet
from dotenv import load_dotenv

from services.config import server_settings

from services.network.getip import get_local_ip
from services.middleware.guards import middleware_guards, is_open_route

from routes.web import web
from routes.api import api
from routes.api import group_api
from routes.automacao import automacao
from routes.automacao import group_automacao
from routes.macro_api import macro_api
from routes.macro_api import group_macro_api


# def start_server(app):
def start_server(app, https=False):    
    load_dotenv()

    hot_reload = bool(os.environ['DEBUGGER'])

    server = server_settings()
    ambiente = server['ambiente']
    https = server['ambiente'] == 'https'
    dominio = server['dominio']
    current_ip = server['ip']
    port = server['porta']

    print('==============================================================')
    print(f'AMBIENTE: {ambiente}')
    print(f'SERVIDOR ATUAL: {dominio}')
    print('==============================================================')

    secret_key = Fernet.generate_key()
    app.secret_key = secret_key.decode()

    if (server['master'] == None):
        @app.before_request
        def load_middleware():
            open_route = is_open_route()
            if (not open_route):
                token = session.get('token')
                if (token == None):
                    return render_template('config/access-denied.html.jinja')
                else:
                    permission = middleware_guards(app.secret_key, token)
                    if (not permission):
                        return render_template('config/access-denied.html.jinja')

                
          
    web(app)
    api(app)
    automacao(app)
    macro_api(app)

    app.register_blueprint(group_api, url_prefix='/api')
    app.register_blueprint(group_automacao, url_prefix='/automacao')
    app.register_blueprint(group_macro_api, url_prefix='/macroapi')

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = '.'
    event_handler = LoggingEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    app.debug=hot_reload
    app.config['JSON_AS_ASCII'] = False

    # # Configuração do registro de logs
    # log_handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=1)
    # log_handler.setLevel(logging.ERROR)
    # formatter = logging.Formatter(
    #     '%(asctime)s [%(levelname)s]: %(message)s [in %(pathname)s:%(lineno)d]'
    # )
    # log_handler.setFormatter(formatter)
    # app.logger.addHandler(log_handler)

    # # Tratamento de erros personalizado para erros 500 (Internal Server Error)
    # @app.errorhandler(500)
    # def internal_server_error(e):
    #     app.logger.error('Erro interno do servidor: %s', e)
    #     return 'Erro interno do servidor', 500


    if (https):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain('cert.pem', 'key.pem')
        app.run(ssl_context=context, host=current_ip, port=port)
    else:
        app.run(host=current_ip, port=port)
        # app.run(host=current_ip, port=80)

    # if (ambiente == 'prod'):
    #     serve(app, host=current_ip, port=port)
    # else:
    #     if (https):
    #         context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #         context.load_cert_chain('cert.pem', 'key.pem')
    #         app.run(ssl_context=context, host=current_ip, port=port)
    #     else:
    #         app.run(host=current_ip, port=80)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()