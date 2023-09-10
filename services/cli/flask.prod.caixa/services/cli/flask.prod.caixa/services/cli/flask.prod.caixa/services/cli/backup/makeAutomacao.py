import sys
import argparse
import kernel.macroAutomacao as macroAutomacao
from kernel.interface import p

try:
    parser = argparse.ArgumentParser(description="Cria automação no servidor.")

    parser.add_argument('elemento_nome', type=str, help="Nome do elemento a ser criado.")
    parser.add_argument('elemento_titulo', type=str, help="Título do elemento a ser criado.")
    parser.add_argument('elemento_desc', type=str, help="Descrição do elemento a ser criado.")
    
    args = parser.parse_args()

    nome = args.elemento_nome
    titulo = args.elemento_titulo.replace("\"","")
    desc = args.elemento_desc.replace("\"","")

    sysMacroAut = macroAutomacao.MacroAut()
    macroExists = sysMacroAut.macroExists(nome)
    routeExists = sysMacroAut.routeExists(nome)

    if (macroExists):
        p(f'Erro na execução. Automação {nome} já registrada.','danger')
        sys.exit()

    if (routeExists):
        p(f'Erro na execução. Rota /{nome} já registrada para outra automação.','danger')
        sys.exit()
    
    # Procede criação
    sysMacroAut.createRoute(nome)
    sysMacroAut.createReadme(nome, titulo, desc)
    sysMacroAut.createMacroAut(nome)
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