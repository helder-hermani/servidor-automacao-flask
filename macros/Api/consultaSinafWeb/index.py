# -*- coding: utf-8 -*-
import os
from time import sleep

from dependencies.loadinfofile import loadInfo
from macros.Api.consultaSinafWeb.sinafwebApi import SinafWebApi

readme = f'{os.path.dirname(os.path.abspath(__file__))}/readme.md'

def info():
    loadInfo(readme)

def index(request):
    params = request.json
    user = params["user"]
    password = params["password"]
    unidadeMovimento = params["unidadeMovimento"]
    conciliacao = params["conciliacao"]
    nomeProponente = params["nomeProponente"]
    valorRP = params["valorRP"]
    dataProposta = params["dataProposta"]

    appSinaf = SinafWebApi()
    resultado = appSinaf.processaConsultaSinafWeb(user, password, unidadeMovimento, conciliacao, nomeProponente, valorRP, dataProposta)
    return resultado