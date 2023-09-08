# -*- coding: utf-8 -*-
from time import sleep
from services.tracker import Tracker
from services.tracker import active_tracks

def start(req_id, req_name, user):
    try:
        t = Tracker()
        t.start(req_id, req_name, user)

        # ---------------------------------------------------------------------
        # Início do bloco de desenvolvimento ----------------------------------
        # ---------------------------------------------------------------------
        
        t.send(req_id,'Macro iniciada')

        qtd_msg = t.select(req_id, 'informe quantas mensagens de boas vindas são suficientes:','5,20,50')
        t.send(req_id, f'Quantidade de mensagens a serem enviadas: {qtd_msg}')
        qtd_msg = int(qtd_msg)

        nome_usuario = t.input(req_id,"Infome seu nome:")
        t.send(req_id, f'Início da macro de testes - Contador de Mensagens - Nome do usuário: <span style="font-size: 1.2rem; color: yellow;">{nome_usuario}</span>')

        # chave = t.inputPassword(req_id,"Infome sua chave de acesso:")
        # t.send(req_id, f'Chave de acesso informada: {chave}')

        # t.send(req_id,"Selecione um arquivo Excel (.xlsx), que contenha uma coluna com o nome FILMES (letras maiúsculas)")
        
        # df = t.dataframe(req_id)

        # for index, row in df.iterrows():
        #     contrato = row['FILMES']
        #     t.send(req_id,f'Filme informado: {contrato}')

        its_enough = False
        counter = 0
        while (its_enough == False):
            counter += 1
            msg = f'Olá, {nome_usuario}! Esta é uma mensagem de boas vindas no terminal. Mensagem número {str(counter)}'
            print(msg)

            if ((counter % 5) == 0):
                style = 'text-info'
            else:
                style = None

            t.send(req_id,msg, style)
            sleep(3)
            if (counter >= qtd_msg):
                its_enough = True

        # --------------------------------------------------------------------
        # Final do bloco de desenvolvimento ----------------------------------
        # --------------------------------------------------------------------
        
        t.end(req_id, 'Macro Finalizada')

        return "Final da execução"
    except Exception as err:
        t.end(req_id, str(err))
        raise err