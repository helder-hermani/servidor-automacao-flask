from flask import render_template, session, request, redirect, url_for

import controllers.Login.login as Login
import controllers.MacrosApi.viewMacrosApi as viewMacrosApi
import controllers.MacrosApi.viewMacro as viewMacro
import controllers.Emulador.emulador as emulador
import controllers.Servers.index as servers
import controllers.Logs.index as Logs
import controllers.Logs.downloadMensagens as LogDownload

def web(app):
    @app.route("/")
    def index():
        return render_template('/index/index.html.jinja')
    
    @app.route("/home")
    def wb_home():
        return servers.index()
        

    @app.post('/dologin')
    def web_dologin():
        return Login.handle_login(app, request)
    
    @app.get('/emulador')
    def web_emulador():
        return emulador.showEmulador()
        # return render_template('emulador/index.html.jinja')
    
    @app.get('/web/macrosapi')
    def web_macrosapi():
        return viewMacrosApi.index()
        # return render_template('emulador/index.html.jinja')

    @app.get('/logs')
    def web_log():
        return Logs.logIndex()
    
    @app.get('/logs/download/mensagens/<id>')
    def web_log_download_msg(id):
        return LogDownload.downloadMensagens(id)
    
    @app.get('/logout')
    def web_logout():
        session['token']=None
        return Login.handle_logout()
    
    @app.get('/web/macroapi/viewMacro')
    def web_viewMacro():
        return viewMacro.index(request)