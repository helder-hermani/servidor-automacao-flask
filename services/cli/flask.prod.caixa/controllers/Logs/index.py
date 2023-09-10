from flask import render_template
import pandas as pd

def logIndex():
    df_log = pd.read_csv('services/logs/requests.log', encoding='utf-8', sep=';')
    df_req = df_log.rename(columns={'id':'id', 'name': 'Nome Processo', 'owner': 'Proprietário', 'lastuser': 'Último uuário', 'msg': 'Mensagem', 'datetime': 'Hora'})
    # filtro = df_log['id'] == idReq
    # df_req = df_log.loc[filtro]
    return render_template('logs/index.html.jinja',df_req=df_req)