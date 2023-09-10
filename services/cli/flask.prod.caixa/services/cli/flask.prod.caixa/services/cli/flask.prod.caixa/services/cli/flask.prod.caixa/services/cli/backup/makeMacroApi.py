import sys
import argparse
import kernel.macroApi as macroApi
from kernel.interface import p

try:
    parser = argparse.ArgumentParser(description="Cria elementos no servidor de aplicações")

    # parser.add_argument('comando', type=str, help="Comando único: make")
    # parser.add_argument('elemento_tipo', type=str, help="Elemento a ser criado. Opções: api, macroApi, automacao.")
    parser.add_argument('elemento_nome', type=str, help="Nome do elemento a ser criado.")
    parser.add_argument('elemento_titulo', type=str, help="Título do elemento a ser criado.")
    parser.add_argument('elemento_desc', type=str, help="Descrição do elemento a ser criado.")
    parser.add_argument('method', type=str, help="Método de chamada do elemento a ser criado (GET ou POST).")
    parser.add_argument('--params', type=str, default='[]', help='Argumentos da chamada do elemento a ser criado. Informe a lista de argumentos entre aspas e entre colchetes. Ex.: "[user, password]"')

    args = parser.parse_args()

    # comando = args.comando
    # tipo = args.elemento_tipo
    nome = args.elemento_nome
    titulo = args.elemento_titulo.replace("\"","")
    desc = args.elemento_desc.replace("\"","")
    metodo = args.method

    if (args.params is not None and args.params != "" and args.params != "\"\""):
        params_list = args.params.replace(" ","")
        params = params_list.replace("\"","").split(",")
    else:
        params = []

    # Cria macroApi
    # if (tipo=="macroApi"):
    sysMacroApi = macroApi.MacroApi()
    macroExists = sysMacroApi.macroExists(nome)
    routeExists = sysMacroApi.routeExists(nome)

    if (macroExists):
        p(f'Erro na execução. Macro {nome} já registrada.','danger')
        sys.exit()

    if (routeExists):
        p(f'Erro na execução. Rota /{nome} já registrada para outro processo.','danger')
        sys.exit()
    
    # Procede criação
    sysMacroApi.createRoute(nome, metodo)
    sysMacroApi.createReadme(nome, titulo, desc, metodo, params)
    sysMacroApi.createMacroApi(nome, metodo, params)
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