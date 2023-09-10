# -*- coding: utf-8 -*-



import macros.Api.consultaSinafWeb.index as consultaSinafWeb

from flask import request, render_template_string, render_template, jsonify, Blueprint
from flask_cors import CORS, cross_origin
import json

group_macro_api = Blueprint('macroapi',__name__)

def macro_api(app):
    pass

    @group_macro_api.post("/consultaSinafWeb")
    def macro_api_consultaSinafWeb():
        try:
            resultado = consultaSinafWeb.index(request)
            return jsonify(resultado), 200
        except Exception as err:
            resultado = {
                "status": "error",
                "message": f'Erro ao processar a requisição: {str(err)}'
            }
            return json.dumps(resultado, ensure_ascii=False).encode('utf-8'), 500
    







