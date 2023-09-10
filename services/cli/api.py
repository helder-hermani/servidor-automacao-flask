import services.cli.kernel.macroApi as macroApi
import services.cli.kernel.macroAutomacao as macroAutomacao

class CliApi:
    def __init__(self) -> None:
        pass

    def makeMacroApi(self, nome, titulo, desc, metodo, args=None):
        try:
            metodo = metodo.lower()
            if (args is not None and args != ""):
                params_list = args.replace(" ","")
                params = params_list.replace("\"","").split(",")
            else:
                params = []

            # Cria macroApi
            sysMacroApi = macroApi.MacroApi()
            macroExists = sysMacroApi.macroExists(nome)
            routeExists = sysMacroApi.routeExists(nome)

            if (macroExists):
                raise Exception(f'Erro na execução. Macro {nome} já registrada.')

            if (routeExists):
                raise Exception(f'Erro na execução. Rota /{nome} já registrada para outro processo.')
            
            # Procede criação
            sysMacroApi.createRoute(nome, metodo)
            sysMacroApi.createReadme(nome, titulo, desc, metodo, params)
            sysMacroApi.createMacroApi(nome, metodo, params)
        
            return {'status': f'MacroApi {nome} registrada com sucesso!'},200
        except Exception as err:
            return str(err),500
        

    def deleteMacroApi(self, nome, metodo):
        try:
            sysMacroApi = macroApi.MacroApi()
            macroExists = sysMacroApi.macroExists(nome)
            routeExists = sysMacroApi.routeExists(nome)

            if (not macroExists):
                raise Exception(f'Erro na execução. Macro {nome} não existe.')

            if (not routeExists):
                raise Exception(f'Erro na execução. Rota /{nome} não existe.')
            
            # Procede remoção
            sysMacroApi.deleteRoute(nome, metodo)
            sysMacroApi.deleteMacroApi(nome)
            return {'status': f'MacroApi {nome} deletada com sucesso!'},200
        except Exception as err:
            return str(err),500
        

    def makeAutomacao(self, nome, titulo, desc):
        try:
            sysMacroAut = macroAutomacao.MacroAut()
            macroExists = sysMacroAut.macroExists(nome)
            routeExists = sysMacroAut.routeExists(nome)

            if (macroExists):
                raise Exception(f'Erro na execução. Automação {nome} já registrada.')

            if (routeExists):
                raise Exception(f'Erro na execução. Rota /{nome} já registrada para outra automação.')
            
            # Procede criação
            sysMacroAut.createRoute(nome)
            sysMacroAut.createReadme(nome, titulo, desc)
            sysMacroAut.createMacroAut(nome)

            return {'status': f'Automação {nome} criada com sucesso!'},200
        except Exception as err:
            return str(err),500
        

    def deleteAutomacao(self, nome):
        try:
            sysMacroAut = macroAutomacao.MacroAut()
            macroExists = sysMacroAut.macroExists(nome)
            routeExists = sysMacroAut.routeExists(nome)

            if (not macroExists):
                raise Exception(f'Erro na execução. Macro {nome} não existe.')

            if (not routeExists):
                raise Exception(f'Erro na execução. Rota /{nome} não existe.')
            
            # Procede remoção
            sysMacroAut.deleteRoute(nome)
            sysMacroAut.deleteMacroAut(nome)
            return {'status': f'Automação {nome} deletada com sucesso!'},200
        except Exception as err:
            return str(err),500

        