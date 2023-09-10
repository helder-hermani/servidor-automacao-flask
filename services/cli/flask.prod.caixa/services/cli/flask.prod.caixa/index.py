# -*- coding: utf-8 -*-
import sys
from flask import Flask
from services.server import start_server
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    start_server(app)
    
    # https=False
    # if (len(sys.argv) > 1):
    #     if (sys.argv[1] == 'https'):
    #         https=True
    # print(f"Execução com certificado SSL: {https}")            
    # start_server(app, https=https)
    # # start_server(app)

