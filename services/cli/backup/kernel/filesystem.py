import os
import shutil

class FileSystem:
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(diretorio_atual, '..', '..','..'))
    
    def __init__(self):
        self.diretorio_atual = self.diretorio_atual
        self.root = self.root
    
    def existsFolder(self, path, folderName):
        folders = [diretorio for diretorio in os.listdir(path) if os.path.isdir(os.path.join(path, diretorio))]

        for folder in folders:
            if (folder == folderName):
                return True

        return False
    
    def existsRoute(self, path, fileName):
        with open(path, 'r', encoding='utf-8') as routes_file:
            for linha in routes_file:
                if (linha.find(f'/{fileName}') >= 0):
                    return True
                
        return False
    
    def createRoute(self, path, import_str, route_block):
        temp_file =''
        add_import=False
        end_imports=False

        with open(path, 'r', encoding='utf-8') as routes_file:
            for linha in routes_file:
                temp_file = temp_file + linha

                if (linha.find('import') < 0 and linha.find('from') < 0 and end_imports==False):
                    add_import = True
                    end_imports = True
                
                if (add_import):
                    temp_file = temp_file + import_str + "\n"
                    add_import = False

        temp_file = temp_file + route_block + "\n" + "\n"

        with open(path,'w',encoding='utf-8') as routes_file:
            routes_file.write(temp_file)

        return temp_file
    
    def createFolder(self, path):
        os.makedirs(path)

    def deleteFolder(self, path):
        shutil.rmtree(path)

    def createFile(self, path, fileName, content):
        with open(f'{path}\\{fileName}', 'w', encoding='utf-8') as file:
            file.write(content)