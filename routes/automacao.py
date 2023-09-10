# -*- coding: utf-8 -*-
from macros.Automacao.novaMacroWeb.home import start as start

from macros.Automacao.minhaApp2.home import start as start
from macros.Automacao.minhaApp1.home import start as start
from flask import render_template_string, render_template, jsonify, Blueprint

group_automacao = Blueprint('automacao',__name__)

def automacao(app):
    pass
    @group_automacao.route("/minhaApp1/<req_id>/<req_name>/<user>")
    def macro_minhaApp1_index(req_id, req_name, user):
        try:
            retorno = start(req_id, req_name, user)
            return retorno
        except Exception as err:
            return str(err), 500
    


    @group_automacao.route("/minhaApp2/<req_id>/<req_name>/<user>")
    def macro_minhaApp2_index(req_id, req_name, user):
        try:
            retorno = start(req_id, req_name, user)
            return retorno
        except Exception as err:
            return str(err), 500
    

    




    @group_automacao.route("/novaMacroWeb/<req_id>/<req_name>/<user>")
    def macro_novaMacroWeb_index(req_id, req_name, user):
        try:
            retorno = start(req_id, req_name, user)
            return retorno
        except Exception as err:
            return str(err), 500
    

