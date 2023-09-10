import sys
import requests

from datetime import datetime, date, timezone, timedelta
# from urllib import request, response
from time import sleep

import json
import urllib3
from urllib.parse import quote

class SinafWebApi:
    def __init__(self, nomeProcesso=""):
        self.nomeProcesso = nomeProcesso
        self.status = 0

    def formataDDMMYYYtoBanco(self, dataStr):
        dataObj = datetime.strptime(dataStr,'%d/%m/%Y')
        dataStr = dataObj.strftime("%Y-%m-%d")
        return dataStr
    
    def validaDlePorNome(self, nome, historico):
        nomesPartes = nome.split(" ")
        nomesIniciais = (nomesPartes[0] + " " + nomesPartes[1]).upper()
        strIndex = historico.upper().find(nomesIniciais)
        if (strIndex >= 0):
            return True
        else:
            return False
   

    def pegaCredenciais(self, user, password):
        # Desativa os logs de aviso do urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Pega token de sessão
        response = requests.get("http://sinafweb.caixa/sinaf3-web", verify=False)
        JSESSIONID = response.cookies

        # Efetua login
        url_login = 'https://sinafweb.caixa/sinaf3-web/login'
        payload = {'j_username':user,'j_password':password}

        responseLogin = requests.post(url_login, data=payload, cookies=JSESSIONID, verify=False)

        # Pega credencias - dados do usuário e ip
        responseUser = requests.get("https://sinafweb.caixa/sinaf3-web/rs/usuario/", cookies=JSESSIONID, verify=False)
        jsonUser = responseUser.json()
        strUser = json.dumps(jsonUser)
        encodedUser = quote(strUser)

        # Define cookies das requisições
        cookies = {
            'JSESSIONID': JSESSIONID['JSESSIONID'],
            'usuario': encodedUser
        }

        # Define cabeçalhos das requisições
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=' + JSESSIONID['JSESSIONID'] + '; usuario=' + encodedUser,
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'sinafweb.caixa',
            'Origin': 'https://sinafweb.caixa',
            'Referer': 'https://sinafweb.caixa/sinaf3-web/',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

        return {"headers":headers,"cookies":cookies}


    def consultaDLE(self, credenciais, unidadeMovimento, conciliacao, nomeProponente, valorRP, dataProposta, sitAutenticada=False):
        result = None
        headers = credenciais['headers']
        cookies = credenciais['cookies']
        # unidadeMovimento = str(registro[20])
        # conciliacao = str(registro[5])
        # nomeProponente = str(registro[2])
        # valorRP = str(registro[10])
        # dataProposta = formata.formataDDMMYYYtoBanco(registro[17]) + "T03:00:00.000Z"
        dataAtual = datetime.today().strftime('%Y-%m-%d')
        dataAtual = str(dataAtual) + "T03:00:00.000Z"

        payload = {
                "qtdResultadosPorPagina":10,
                "pagina":1,
                "todosSelecionados":False,
                "documentosSelecionados":[],
                "sgDcmtoLancamentoContabil":"DLE",
                "mesDocumento":None,
                "anoDocumento":None,
                "nuUnidadeMovimento":unidadeMovimento,
                "coConciliacao":conciliacao,
                "dtMovimentoDocumentoInicial":dataProposta,
                "dtMovimentoDocumentoFinal":dataAtual,
            }
        
        
        if (sitAutenticada == True):
            payload['nuEstadoDocumentoContabil'] = 11

        responseQtd = requests.post('https://sinafweb.caixa/sinaf3-web/rs/documento-lancamento/recuperar-documento/quantidade', json=payload, cookies=cookies, headers=headers, verify=False)
        responseData = requests.post('https://sinafweb.caixa/sinaf3-web/rs/documento-lancamento/recuperar-documento', json=payload, cookies=cookies, headers=headers, verify=False)

        if (int(responseQtd.text) == 0):
            result = None
        else:
            for dle in responseData.json():
                historico = dle['deHistorico']
                vlrLancamento = dle['vlrLancamento']
                validaNome = self.validaDlePorNome(nomeProponente, historico)

                if (validaNome and (float(valorRP) == float(vlrLancamento))):
                    result = dle
        
        return result

    def processaConsultaSinafWeb(self, user, password, unidadeMovimento, conciliacao, nomeProponente, valorRP, dataProposta):
        credenciais = self.pegaCredenciais(user,password)

        unidadeMovimento=str(unidadeMovimento)
        conciliacao=str(conciliacao)
        nomeProponente=str(nomeProponente)
        valorRP=str(valorRP)
        dataProposta = self.formataDDMMYYYtoBanco(dataProposta) + "T03:00:00.000Z"

        # print(credenciais)

        resolveDleAuth = self.consultaDLE(credenciais,unidadeMovimento, conciliacao, nomeProponente, valorRP, dataProposta,True)

        if (resolveDleAuth != None):    #DLE está autenticada
            numDle = resolveDleAuth['nuDocumento']
            novaSituacaoDLE = resolveDleAuth['noEstadoDocumentoContabil'].strip()
            valorDle = resolveDleAuth['vlrLancamento']
            codAgencia = resolveDleAuth['nuUnidadeMovimento']

            # print(resolveDleAuth)
        else: #DLE não está autenticada
            resolveDle = self.consultaDLE(credenciais,unidadeMovimento, conciliacao, nomeProponente, valorRP, dataProposta,False)
            numDle = resolveDleAuth['nuDocumento']
            novaSituacaoDLE = resolveDleAuth['noEstadoDocumentoContabil'].strip()
            valorDle = resolveDleAuth['vlrLancamento']
            codAgencia = resolveDleAuth['nuUnidadeMovimento']

            # print(resolveDleAuth)

        return {
            'numDle' : numDle,
            'novaSituacaoDLE' : novaSituacaoDLE,
            'valorDle' : valorDle,
            'codAgencia' : codAgencia
        }

        
            
            
    
    