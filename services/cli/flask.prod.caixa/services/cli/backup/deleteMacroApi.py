import sys
import argparse
import kernel.macroApi as macroApi
from kernel.interface import p

try:
    parser = argparse.ArgumentParser(description="Deleta elementos no servidor de aplicações")

    # parser.add_argument('comando', type=str, help="Comando único: delete")
    # parser.add_argument('elemento_tipo', type=str, help="Tipo de elemento a ser deletado. Opções: api, macroApi, automacao.")
    parser.add_argument('elemento_nome', type=str, help="Nome do elemento a ser deletado.")
    parser.add_argument('elemento_method', type=str, help="Confirme o método de requisição do elemento a ser deletado.")
    
    args = parser.parse_args()

    # comando = args.comando
    # tipo = args.elemento_tipo
    nome = args.elemento_nome
    metodo = args.elemento_method
    
    # Deleta macroApi
    # if (tipo=="macroApi"):
    print("")
    p('ATENÇÃO!','danger')
    print("")
    confirm = input(f"Este comando irá DELETAR a Macro Api {nome}. Este processo é IRREVERSÍVEL. Deseja continuar (s/n)?")
    print("")

    if (confirm.upper()=='S'):
        sysMacroApi = macroApi.MacroApi()
        macroExists = sysMacroApi.macroExists(nome)
        routeExists = sysMacroApi.routeExists(nome)

        if (not macroExists):
            p(f'Erro na execução. Macro {nome} não existe.','danger')
            sys.exit()

        if (not routeExists):
            p(f'Erro na execução. Rota /{nome} não existe.','danger')
            sys.exit()
        
        # Procede remoção
        sysMacroApi.deleteRoute(nome, metodo)
        sysMacroApi.deleteMacroApi(nome)
        print('')
        print('-------------------------------')
        p('COMANDO EXECUTADO COM SUCESSO!','success')
        print('-------------------------------')
        print('')
    # elif (tipo=="api"):
    #     pass
    # elif (tipo=="automacao"):
    #     pass
    # else:
    #     print('Tipo não reconhecido')

    # print(comando)
    # print(tipo)
    # print(nome)
    # print(titulo)
    # print(desc)
    # print(metodo)
    # print(params)
except Exception as err:
    print('-------------------------------')
    print('ERRO NA EXECUÇÃO')
    print('-------------------------------')
    print(f'Erro no comando. {err}')
    
    
    # Criar macro API