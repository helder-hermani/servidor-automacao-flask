import sys
import argparse
import kernel.macroAutomacao as macroAutomacao
from kernel.interface import p

try:
    parser = argparse.ArgumentParser(description="Deleta elementos no servidor de aplicações")
    parser.add_argument('elemento_nome', type=str, help="Nome da automação a ser deletado.")

    
    args = parser.parse_args()

    nome = args.elemento_nome

    print("")
    p('ATENÇÃO!','danger')
    print("")
    confirm = input(f"Este comando irá DELETAR a Macro Api {nome}. Este processo é IRREVERSÍVEL. Deseja continuar (s/n)?")
    print("")

    if (confirm.upper()=='S'):
        sysMacroAut = macroAutomacao.MacroAut()
        macroExists = sysMacroAut.macroExists(nome)
        routeExists = sysMacroAut.routeExists(nome)

        if (not macroExists):
            p(f'Erro na execução. Macro {nome} não existe.','danger')
            sys.exit()

        if (not routeExists):
            p(f'Erro na execução. Rota /{nome} não existe.','danger')
            sys.exit()
        
        # Procede remoção
        sysMacroAut.deleteRoute(nome)
        sysMacroAut.deleteMacroAut(nome)
        print('')
        print('-------------------------------')
        p('COMANDO EXECUTADO COM SUCESSO!','success')
        print('-------------------------------')
        print('')
  
except Exception as err:
    print('-------------------------------')
    print('ERRO NA EXECUÇÃO')
    print('-------------------------------')
    print(f'Erro no comando. {err}')
    
    
    # Criar macro API