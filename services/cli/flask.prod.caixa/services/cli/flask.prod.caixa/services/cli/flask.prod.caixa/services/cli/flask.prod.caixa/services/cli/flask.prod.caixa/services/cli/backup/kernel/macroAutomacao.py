import os
import sys

import kernel.filesystem as filesystem
import kernel.mirrors.mirrorAutomacao as mirrorAutomacao

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..', '..', '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings

class MacroAut:
    def __init__(self):
        pass

    def macroExists(self, macroName):
        system = filesystem.FileSystem()
        root = system.root
        appPath = '\\macros\\Automacao'

        exists = system.existsFolder(f'{root}{appPath}',macroName)

        return exists
    
    def routeExists(self, macroName):
        system = filesystem.FileSystem()
        root = system.root
        filePath = '\\routes\\automacao.py'

        exists = system.existsRoute(f'{root}{filePath}',macroName)

        return exists
    
    def generateImport(self, macroName):
        mirror = mirrorAutomacao.MirrorMacroAut(macroName)
        return mirror.generateImport()
    
    def generateRoute(self, macroName):
        mirror = mirrorAutomacao.MirrorMacroAut(macroName)
        return mirror.generateRoute()
    
    def createRoute(self, macroName):
        system = filesystem.FileSystem()
        root = system.root
        filePath = f'{root}\\routes\\automacao.py'

        import_str = self.generateImport(macroName)
        route_block = self.generateRoute(macroName)
        
        return system.createRoute(filePath, import_str, route_block)
    
    def createReadme(self, nome, titulo, desc):
        system = filesystem.FileSystem()
        root = system.root
        
        current_path = system.diretorio_atual

        # server = server_settings()
        # dominio = server['dominio']
        
        with open(f'{current_path}\\mirrors\\modelos\\automacao_readme.mir','r',encoding='utf-8') as readme:
            readme_content = readme.read()
            readme_content = readme_content.replace('-->nome<--', nome)
            readme_content = readme_content.replace('-->titulo<--', titulo)
            readme_content = readme_content.replace('-->desc<--', desc)
            readme_content = readme_content.replace('-->rota<--', f'/automacao/{nome}')
            
        new_readme_path = f'{root}\\macros\\Automacao\\{nome}'
        system.createFolder(new_readme_path)
        system.createFile(new_readme_path,'readme.md',readme_content)
        return readme_content
    
    def createMacroAut(self, nome):
        system = filesystem.FileSystem()
        current_path = system.diretorio_atual
        root = system.root
        new_readme_path = f'{root}\\macros\\Automacao\\{nome}'

        with open(f'{current_path}\\mirrors\\modelos\\automacao_controller.mir','r',encoding='utf-8') as macro_aut:
            content = macro_aut.read()
            # tab_space = "    "
                    
            system.createFile(new_readme_path,'home.py',content)

    def deleteRoute(self, macroName):
        system = filesystem.FileSystem()
        root = system.root
        filePath = f'{root}\\routes\\automacao.py'

        import_str = self.generateImport(macroName)
        route_block = self.generateRoute(macroName)
        
        with open(filePath,'r',encoding='utf-8') as file_route:
            content = file_route.read()
            content = content.replace(import_str,"")
            content = content.replace(route_block,"")
        
        with open(filePath,'w',encoding='utf-8') as file_route:
            file_route.write(content)


    def deleteMacroAut(self, nome):
        system = filesystem.FileSystem()
        root = system.root
        
        macro_path = f'{root}\\macros\\Automacao\\{nome}'
        system.deleteFolder(macro_path)
        
    