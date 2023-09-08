from flask import jsonify, Blueprint, session, render_template, request, abort
import json
import pandas as pd

from services.tracker import active_tracks
import services.tracker as Tracker
import controllers.Login.login as Login
import controllers.Emulador.emulador as Emulador

group_api = Blueprint('api',__name__)

def api(app):
    @group_api.route("/")
    def api_index():
        status = {'status':'OK'}
        return json.dumps(status, ensure_ascii=False).encode('utf-8')
    
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
        
    # @group_api.post('/emulador/upload_excel')
    # def emulador_upload_excel():
    #     try:
    #         if ('file' not in request.files):
    #             return jsonify({'error': 'Nenhum arquivo enviado'})

    #         file = request.files['file']

    #         df = pd.read_excel(file)
    #         print(df)

    #         return jsonify({'status': 'Arquivo Excel recebido e processado com sucesso'})
    #     except Exception as err:
    #         return f'Erro na execução. {str(err)}',500