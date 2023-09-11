from flask import jsonify, Blueprint, session, render_template, request, abort
import json
import pandas as pd

from services.tracker import active_tracks
import services.tracker as Tracker
import controllers.Login.login as Login
import controllers.Emulador.emulador as Emulador
import controllers.Servers.ping as Ping
import controllers.Cli.macroApi as CliMacroApi
import controllers.Cli.macroAutomacao as CliMacroAutomacao
import controllers.Deploy.index as Deploy

group_api = Blueprint('api',__name__)

def api(app):
    @group_api.route("/")
    def api_index():
        try:
            return jsonify(Ping.ping()),200
        except Exception as err:
            return str(err), 500
        # status = {'status':'OK'}
        # return json.dumps(status, ensure_ascii=False).encode('utf-8')
    
    @group_api.post("/dologin")
    def dologin():   
        return Login.handle_login(app, request)
    

    @group_api.get("/emulador/macroinfo/<macroName>")
    def emulador_macro_info(macroName):   
        return Emulador.getMacroInfo(macroName)
    
    @group_api.get("/emulador/play/<macroName>")
    def emulador_macro_play(macroName):   
        try:
            return jsonify(Emulador.macroPlay(macroName))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get("/emulador/stop/<reqId>/<user>")
    def emulador_macro_stop(reqId, user):   
        try:
            return jsonify(Tracker.stopMacro(reqId, user))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get("/emulador/pause/<reqId>/<user>")
    def emulador_macro_pause(reqId, user):   
        try:
            return jsonify(Tracker.pauseMacro(reqId, user))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get("/emulador/restart/<reqId>")
    def emulador_macro_restart(reqId):   
        try:
            return jsonify(Tracker.restartMacro(reqId))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
   
    
    @group_api.route("/tracker/gettracks")
    def get_all_tracks():
        return json.dumps(active_tracks, ensure_ascii=False).encode('utf-8')


    @group_api.route("/tracker/getReqInfo/<reqId>")
    def get_req_info(reqId):
        return jsonify(Tracker.getTrack(reqId))

        
    @group_api.route("/tracker/getMessages/<reqId>")
    def track_getMessages(reqId):
        try:
            return jsonify(Tracker.getMessages(reqId))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get("/tracker/answerInput/<reqId>/<answer>")
    def track_answerInput(reqId, answer):
        try:
            return jsonify(Tracker.answerInput(reqId, answer))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get("/tracker/answerInputPassword/<reqId>/<answer>")
    def track_answerInputPassword(reqId, answer):
        try:
            return jsonify(Tracker.answerInputPassword(reqId, answer))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500

    @group_api.get("/tracker/answerSelect/<reqId>/<answer>")
    def track_answerSelect(reqId, answer):
        try:
            return jsonify(Tracker.answerSelect(reqId, answer))
        except Exception as err:
            return f'Erro na execução. {str(err)}',500


    @group_api.post('/emulador/upload_excel/<reqId>')
    def emulador_upload_excel(reqId):
        try:
            return Tracker.answerDataFrame(request, reqId)
            # return jsonify({'status': 'Arquivo Excel recebido e processado com sucesso'})
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.post('/cli/make/macroApi')
    def cli_make_macro_api():
        try:
            return CliMacroApi.make(request)
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.post('/cli/delete/macroApi')
    def cli_delete_macro_api():
        try:
            return CliMacroApi.delete(request)
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.post('/cli/make/automacao')
    def cli_make_automacao_api():
        try:
            return CliMacroAutomacao.make(request)
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.post('/cli/delete/automacao')
    def cli_delete_automacao_api():
        try:
            return CliMacroAutomacao.delete(request)
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get('/deploy/backup/<servidor_destino>')
    def cli_deploy_backup(servidor_destino):
        try:
            return jsonify(Deploy.makeBackup(servidor_destino)), 200
        except Exception as err:
            return f'Erro na execução. {str(err)}',500
        
    @group_api.get('/deploy/transferencia/<servidor_destino>/<use_ignore>')
    def cli_deploy_transferencia(servidor_destino, use_ignore):
        try:
            return jsonify(Deploy.makeDeploy(servidor_destino, use_ignore)), 200
        except Exception as err:
            return f'Erro na execução. {str(err)}',500