def getMacroInfo(path):
    iName = 0
    iTitle = 0
    iDesc = 0
    iRoute = 0

    counter = 0
    arrLinhas = []
    readme_path = path + '\\readme.md'
    with open(readme_path, 'r', encoding='utf-8') as readme:
        for linha in readme:
            arrLinhas.append(linha.strip())
            if (linha.find('# Nome') >= 0):
                iName = counter
            if (linha.find('# Titulo') >= 0):
                iTitle = counter
            if (linha.find('# Descrição') >= 0):
                iDesc = counter
            if (linha.find('# Rota') >= 0):
                iRoute = counter
            counter = counter + 1
    
    return {
        'name' : arrLinhas[iName+1],
        'title' : arrLinhas[iTitle+1],
        'desc' : arrLinhas[iDesc+1],
        'route' : arrLinhas[iRoute+1],
        'readme' : readme_path,
        'filepath': path + '\\index.py'
    }

def loadInfo(file):
    with open(file, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    return conteudo

