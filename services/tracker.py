import sys
import os
from time import sleep
from datetime import datetime
from flask import jsonify
import pandas as pd
from bs4 import BeautifulSoup

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings

active_tracks = []

class Tracker:
    def __init__(self):
        self.maxWait = 20

    def start(self, id, name, user):
        objReq = {
            'id': id,
            'name': name,
            'pause': False,
            'abort': False,
            'broken': False,
            'lastOutputIndex': 0,
            'outputs': [],
            'mensagens': [],
            'input': None,
            'inputPassword': None,
            'question': None,
            'dataframe': None,
            'select': None,
            'owner': user,
            'starttime': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'lastuser': user
        }
        
        self.savelog(objReq,'Macro Iniciada')
        active_tracks.append(objReq)
    

    def end(self, track_id, msg='Sem registro'):
        current_track = list(filter(lambda obj: obj['id'] == track_id, active_tracks))
        self.savelog(current_track[0],msg)
        self.saveHistory(current_track[0])
        active_tracks.remove(current_track[0])


    def checkStatusReq(self, idReq):
        for req in active_tracks:
            if (req['id'] == idReq):
                while (req['pause'] == True):
                    sleep(3)
                
                if (req['abort'] == True):
                    print('Macro interrompida pelo usuário')
                    raise Exception("Execução interrompida por solicitação do usuário.")

                

    def send(self, idReq, msg, textClass=None):
        objReq = list(filter(lambda obj: obj['id'] == idReq, active_tracks))

        self.checkStatusReq(idReq)

        if (len(objReq) > 0):
            if (textClass == None):
                textClass='text-light'

            current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            objReq = objReq[0]
            objReq['outputs'].append(f'<span style="color: rgba(255,255,255,.2); margin-right: .5rem; font-size: .8rem;">{current_time} </span><span class="{textClass}">{msg}</span>')
        else:
            return None
        
    def input(self, idReq, question):
        for req in active_tracks:
            if (req['id'] == idReq):

                # Espera limpar o buffer de mensagens enviadas
                while (req['lastOutputIndex'] != len(req['outputs'])):
                    sleep(1)

                req['question'] = {
                    'ask': question,
                    'answer': None
                }

                counter = 0
                while (req['question'] != None and req['question']['answer'] == None):
                    print('Aguardando resposta - método input')
                    counter += 1
                    if (counter >= self.maxWait):
                        raise Exception("Tempo excedido de espera. Macro encerrada.")
                    sleep(3)

                resposta = req['question']['answer']
                req['question'] = None
                return resposta
            
    def inputPassword(self, idReq, question):
        for req in active_tracks:
            if (req['id'] == idReq):

                # Espera limpar o buffer de mensagens enviadas
                while (req['lastOutputIndex'] != len(req['outputs'])):
                    sleep(1)

                req['inputPassword'] = {
                    'ask': question,
                    'answer': None
                }

                counter = 0
                while (req['inputPassword'] != None and req['inputPassword']['answer'] == None):
                    print('Aguardando resposta - input password')
                    counter += 1
                    if (counter >= self.maxWait):
                        raise Exception("Tempo excedido de espera. Macro encerrada.")
                    sleep(3)

                resposta = req['inputPassword']['answer']
                req['inputPassword'] = None
                return resposta

    def select(self, idReq, question, options):
        for req in active_tracks:
            if (req['id'] == idReq):

                # Espera limpar o buffer de mensagens enviadas
                while (req['lastOutputIndex'] != len(req['outputs'])):
                    sleep(1)

                req['select'] = {
                    'ask': question,
                    'options': options,
                    'answer': None
                }

                counter = 0
                while (req['select'] != None and req['select']['answer'] == None):
                    print('Aguardando resposta - answer')
                    counter += 1
                    if (counter >= self.maxWait):
                        raise Exception("Tempo excedido de espera. Macro encerrada.")
                    sleep(3)

                resposta = req['select']['answer']
                req['select'] = None
                return resposta

            
    def dataframe(self, idReq):
        for req in active_tracks:
            if (req['id'] == idReq):

                # Espera limpar o buffer de mensagens enviadas
                while (req['lastOutputIndex'] != len(req['outputs'])):
                    sleep(1)

                sleep(1)

                req['dataframe'] = {
                    'askFile': True,
                    'hasAnswer': None,
                    'answer': pd.DataFrame()
                }

                counter = 0
                while (req['dataframe'] != None and req['dataframe']['hasAnswer'] == None):
                    print('Aguardando resposta - arquivo')
                    counter += 1
                    if (counter >= self.maxWait):
                        raise Exception("Tempo excedido de espera. Macro encerrada.")
                    sleep(3)
                    sleep(3)

                resposta = req['dataframe']['answer']
                req['dataframe'] = None

                return resposta


    def savelog(self, req, msg):
        server = server_settings()
        dominio = server['dominio']
        id = req['id']
        name = req['name']
        owner = req['owner']
        lastuser = req['lastuser']
        moment = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        caminho_arquivo = 'services/logs/requests.log'

        print(f'{id};{name};{owner};{msg};{moment}\n')
        with open(caminho_arquivo,'a',encoding='utf-8') as log:
            log.write(f'{dominio};{id};{name};{owner};{lastuser};{msg};{moment}\n')

    def saveHistory(self, req):
        id = req['id']
        caminho_arquivo = f'static/app/logs/history/{id}.log'
        
        with open(caminho_arquivo,'a',encoding='utf-8') as log:
            for msg in req['outputs']:
                soup = BeautifulSoup(msg,'html.parser')
                msglog = soup.getText()
                log.write(f'{msglog}\n')
            
    

# MÉTODOS
def getMessages(idReq):
    # try:
        for req in active_tracks:
            if (req['id'] == idReq):
                hasQuestion = False
                hasFile = False
                hasPassword = False
                hasSelect = False
                options = None
                historico=None
            
                # Verica se tem requisição da macro para o cliente
                if (req['question'] != None and req['question']['answer'] == None):
                    hasQuestion = True
                    outputs = [req['question']['ask']]
                elif (req['inputPassword'] != None and req['inputPassword']['answer'] == None):
                    hasPassword = True
                    outputs = [req['inputPassword']['ask']]
                elif (req['dataframe'] != None and req['dataframe']['hasAnswer'] == None):
                    hasFile = True
                    outputs = ['Selecione o arquivo Excel (.xlsx):']
                elif (req['select'] != None and req['select']['answer'] == None):
                    hasSelect = True
                    str_options = req['select']['options']
                    options = str_options.split(",")
                    outputs = [req['select']['ask']]
                else:
                    # Prossegue interação normal
                    lastIndex = req['lastOutputIndex']
                    # outputs = req['outputs']
                    outputs = req['outputs'][lastIndex:]
                    historico = req['outputs']
                    req['lastOutputIndex'] = len(req['outputs'])
                    # req['lastOutputIndex'] = len(req['outputs'])-1

                return {
                    'outputs':outputs,
                    'historico': historico,
                    'hasQuestion':hasQuestion,
                    'hasFile':hasFile,
                    'hasPassword':hasPassword,
                    'hasSelect': hasSelect,
                    'options': options,
                    'finallog': None,
                    'lastOutputIndex': req['lastOutputIndex'],
                    # 'properties': req
                    'properties': {
                        'id': req['id'],
                        'name': req['name'],
                        'owner': req['owner'],
                        'starttime': req['starttime'],
                        'lastuser': req['lastuser'],
                        'pause': req['pause'],
                        'abort': req['abort'],
                        'lastOutputIndex': req['lastOutputIndex'],
                        'input': req['input'],
                        'inputPassword': req['inputPassword'],
                        # 'dataframe': req['dataframe'],
                        'select': req['select'],
                        }
                    }

        # Retorna log se a trilha não foi localizada
        df_log = pd.read_csv('services/logs/requests.log', encoding='utf-8', sep=';')

        filtro = df_log['id'] == idReq
        df_req = df_log.loc[filtro]

        df_req = df_req.rename(columns={'id':'id', 'name': 'Nome Processo', 'owner': 'Proprietário', 'lastuser': 'Último uuário', 'msg': 'Mensagem', 'datetime': 'Hora'})
        saida_html = df_req.to_html(index=False)     
        return {
                    'outputs':None,
                    'mensagens':None,
                    'hasQuestion':None,
                    'hasFile':None,
                    'hasPassword':None,
                    'hasSelect': None,
                    'options': None,
                    'finallog': saida_html,
                    'lastOutputIndex': None,
                    'properties': None
                    }
    # except Exception as err:
    #     return err
        
def getTrack(idReq):
    for req in active_tracks:
        if (req['id'] == idReq):
            return req
    
    # Retorno se não estiver na fila
    objReq = {
            'id': None,
            'name': None,
            'pause': None,
            'abort': None,
            'broken': None,
            'lastOutputIndex': None,
            'outputs': None,
            'mensagens': None,
            'input': None,
            'inputPassword': None,
            'question': None,
            'dataframe': None,
            'select': None,
            'owner': None,
            'starttime': None,
            'lastuser': None
        }
    return objReq

def stopMacro(idReq, user):
    for req in active_tracks:
        if (req['id'] == idReq):
            req['abort'] = True
            req['lastuser'] = user
            return {'mensagens':'Macro interrompida pelo usuário'}
        
def pauseMacro(idReq, user):
    for req in active_tracks:
        if (req['id'] == idReq):
            req['pause'] = True
            req['lastuser'] = user
            return {'mensagens':'Macro PAUSADA, por solicitação do usuário.'}
        
def restartMacro(idReq):
    for req in active_tracks:
        if (req['id'] == idReq):
            req['pause'] = False
            return {'mensagens':'Macro REINICIADA, por solicitação do usuário.'}
        
def answerInput(idReq, answer):
    for req in active_tracks:
        if (req['id'] == idReq):
            req['question']['answer'] = answer
            return {'mensagens':'Resposta recebida pelo servidor.'}
        
def answerInputPassword(idReq, answer):
    for req in active_tracks:
        if (req['id'] == idReq):
            req['inputPassword']['answer'] = answer
            return {'mensagens':'Resposta recebida pelo servidor.'}

def answerSelect(idReq, answer):
    for req in active_tracks:
        if (req['id'] == idReq):
            req['select']['answer'] = answer
            return {'mensagens':'Resposta recebida pelo servidor.'}
        
def answerDataFrame(request, idReq):
    if ('file' not in request.files):
        return jsonify({'error': 'Nenhum arquivo enviado'})

    file = request.files['file']

    df = pd.read_excel(file)
    # print(df)

    for req in active_tracks:
        if (req['id'] == idReq):
            req['dataframe']['hasAnswer'] = True
            req['dataframe']['answer'] = df
            return {'mensagens':'Arquivo Excel recebido e processado pelo servidor.'}
