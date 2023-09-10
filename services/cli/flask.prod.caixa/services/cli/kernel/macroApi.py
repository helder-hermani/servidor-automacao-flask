import os
import sys

import services.cli.kernel.filesystem as filesystem
import services.cli.kernel.mirrors.mirrorMacroApi as mirrorMacroApi
from services.config import server_settings

# diretorio_atual = os.path.dirname(__file__)
# diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..', '..'))
# sys.path.append(diretorio_pai)
# from services.config import server_settings

class MacroApi:
    def __init__(self):
        pass

    def macroExists(self, macroName):
        system = filesystem.FileSystem()
        root = system.root
        appPath = '\\macros\\Api'

        exists = system.existsFolder(f'{root}{appPath}',macroName)

        return exists
    
    def routeExists(self, macroName):
        system = filesystem.FileSystem()
        root = system.root
        filePath = '\\routes\\macro_api.py'

        exists = system.existsRoute(f'{root}{filePath}',macroName)

        return exists
    
    def generateImport(self, macroName):
        mirror = mirrorMacroApi.MirrorMacroApi(macroName)
        return mirror.generateImport()
    
    def generateRoute(self, macroName, metodo):
        mirror = mirrorMacroApi.MirrorMacroApi(macroName)
        return mirror.generateRoute(metodo)
    
    def createRoute(self, macroName, metodo):
        system = filesystem.FileSystem()
        root = system.root
        filePath = f'{root}\\routes\\macro_api.py'

        import_str = self.generateImport(macroName)
        route_block = self.generateRoute(macroName, metodo)
        
        return system.createRoute(filePath, import_str, route_block)
    
    def createReadme(self, nome, titulo, desc, metodo, params):
        system = filesystem.FileSystem()
        root = system.root
        # sys.path.append(f'{root}\\services\\network')
        # import getip

        current_path = system.diretorio_atual
        # with open(f'{current_path}\\mirrors\\modelos\\readme.md','r',encoding='utf-8') as readme:
        with open(f'{current_path}\\mirrors\\modelos\\macroApi_readme.mir','r',encoding='utf-8') as readme:
            readme_content = readme.read()
            readme_content = readme_content.replace('-->nome<--', nome)
            readme_content = readme_content.replace('-->titulo<--', titulo)
            readme_content = readme_content.replace('-->desc<--', desc)
            # server = server_settings()
            # dominio = server['dominio']
            readme_content = readme_content.replace('-->rotaApi<--', f'/macroapi/{nome}')
            # readme_content = readme_content.replace('-->rotaApi<--', f'{dominio}/macroapi/{nome}')
            # readme_content = readme_content.replace('-->rotaApi<--', f'http://{getip.get_local_ip()}:7077/macroapi/{nome}')
            readme_content = readme_content.replace('-->metodo<--', metodo.upper())
            params_list=""
            for param in params:
                params_list = f'{params_list}- {param}\n'
            readme_content = readme_content.replace('-->parametros<--', params_list)

        new_readme_path = f'{root}\\macros\\Api\\{nome}'
        system.createFolder(new_readme_path)
        system.createFile(new_readme_path,'readme.md',readme_content)
        return readme_content
    
    def createMacroApi(self, nome, metodo, params):
        system = filesystem.FileSystem()
        current_path = system.diretorio_atual
        root = system.root
        new_readme_path = f'{root}\\macros\\Api\\{nome}'

        with open(f'{current_path}\\mirrors\\modelos\\macroApi.mir','r',encoding='utf-8') as macro_api:
            content = macro_api.read()
            tab_space = "    "
            
            if (metodo.upper()=="GET"):
                params_list = 'params = request.args\n'
                for param in params:
                    params_list = f"{params_list}{tab_space}{param} = params.get(\"{param}\")\n"
                content = content.replace('-->parametros<--', params_list)
            elif (metodo.upper()=="POST"):
                params_list = 'params = request.json\n'
                for param in params:
                    params_list = f"{params_list}{tab_space}{param} = params[\"{param}\"]\n"
                content = content.replace('-->parametros<--', params_list)

            if (len(params) == 0):
                content = content.replace('-->resultado<--', "resultado = {'status':'ok'}")
            else:
                params_list=''
                for param in params:
                    params_list = f"{params_list}{tab_space}{tab_space}\"{param}\" : {param},\n"

                resultado = f"resultado = {{\n{params_list}{tab_space}}}"
                content = content.replace('-->resultado<--', resultado)



                    
            system.createFile(new_readme_path,'index.py',content)

    def deleteRoute(self, macroName, metodo):
        system = filesystem.FileSystem()
        root = system.root
        filePath = f'{root}\\routes\\macro_api.py'

        import_str = self.generateImport(macroName)
        route_block = self.generateRoute(macroName, metodo)
        
        with open(filePath,'r',encoding='utf-8') as file_route:
            content = file_route.read()
            content = content.replace(import_str,"")
            content = content.replace(route_block,"")
        
        with open(filePath,'w',encoding='utf-8') as file_route:
            file_route.write(content)


    def deleteMacroApi(self, nome):
        system = filesystem.FileSystem()
        root = system.root
        
        macro_path = f'{root}\\macros\\Api\\{nome}'
        system.deleteFolder(macro_path)
        
    