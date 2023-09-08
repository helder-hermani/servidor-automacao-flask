import sys
import os

diretorio_atual = os.path.dirname(__file__)
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, '..'))
sys.path.append(diretorio_pai)
from services.config import server_settings

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
            if (linha.find('# Rota View') >= 0):
                iRoute = counter
            counter = counter + 1
    
    return {
        'name' : arrLinhas[iName+1],
        'title' : arrLinhas[iTitle+1],
        'desc' : arrLinhas[iDesc+1],
        'route' : arrLinhas[iRoute+1].replace('- ',''),
        'readme' : readme_path,
        'filepath': path + '\\index.py'
    }

def loadInfo(file):
    with open(file, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    return conteudo


def getInfoRequest(file):
    foundName = False
    foundRotaApi = False
    foundMetodo = False
    foundParams = False

    nome = ''
    rotaApi = ''
    metodo = ''
    params = []

    with open(file, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if (foundName):
                nome = linha.strip()
                foundName = False

            if (foundRotaApi):
                rotaApi = linha[2:len(linha)].strip()
                # rotaApi = linha.strip()
                foundRotaApi = False

            if (foundMetodo):
                # metodo = linha.strip()
                metodo = linha[2:len(linha)].strip()
                foundMetodo = False

            if (foundParams):
                if (linha.find('-') == 0):
                    params.append(linha[2:len(linha)].strip())
                else:
                    foundParams = False

            if (linha.find('# Nome') >= 0):
                foundName = True

            if (linha.find('# Rota API') >= 0):
                foundRotaApi = True

            if (linha.find('# Método Http') >= 0):
                foundMetodo = True

            if (linha.find('# Parâmetros') >= 0):
                foundParams = True

    server = server_settings()
    dominio = server['dominio']
    
    return {
        'nome': nome,
        'dominio': dominio,
        'rotaApi': rotaApi,
        'metodo': metodo,
        'params': params
    }

def generateHtmlSnippet(file):
    dados = getInfoRequest(file)

    form_fields = ""
    for param in dados['params']:
        form_fields = form_fields + f"""&lt;div&gt;{param}:&lt;/div&gt;&lt;div&gt;&lt;input type="{'password' if param == 'password' else 'text'}" name='{param}'/&gt;&lt;/div&gt;\n                    """

    # if (dados['metodo'].upper() == 'POST'):
    #     csrf = '@csrf'
    # else:
    #     csrf = ''

    htmlSnippet = f"""
        &lt;div class='frame-request'&gt;
            &lt;form method='{dados['metodo']}' action='/api/servidorApp/{dados['nome']}' id='form-request'&gt;
                @csrf
                &lt;div class='form-request'&gt;    
                    {form_fields}&lt;div&gt;&lt;/div&gt;
                    &lt;div class='div-btn-request'&gt;
                        &lt;button type='submit' class='btn btn-success'&gt;
                            Executar
                        &lt;/button&gt;
                        &lt;div id='spinner-request' class='spinner-border text-info d-none' role='status'&gt;
                            &lt;span class='sr-only'&gt;Loading...&lt;/span&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;/div&gt;
            &lt;/form&gt;
            &lt;div id='frame-retorno' class='frame-retorno my-3'&gt;&lt;/div&gt;
        &lt;/div&gt;
    """
    return htmlSnippet.strip()

def generateCssSnippet(file):
    cssSnippet = f"""
    &lt;style&gt;
        .frame-request{{
            width: 100%;
            padding: 1rem;
            background-color: rgba(255, 255, 255, .5);
        }}

        .frame-retorno{{
            width: 100%;
            border: solid 2px rgba(0, 0, 0, .05);
            padding: 1rem;
        }}

        .form-request{{
            width: 40%;
            display: grid;
            grid-template-columns: 6fr 6fr;
            gap: 2px;
        }}

        .form-request input{{
            width: 100%;
        }}

        .div-btn-request{{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-evenly;
        }}

        .div-btn-request button{{
            width: 80%;
        }}
    &lt;/style&gt;
    """
    return cssSnippet.strip()

def generateJsSnippet(file):
    jsSnippet = f"""
    &lt;script&gt;
        $(document).ready(function() {{
            $("#form-request").submit(function(event) {{
                event.preventDefault();

                $('#spinner-request').removeClass('d-none')

                var formData = {{}};

                $(this).serializeArray().forEach(function(item){{
                    formData[item.name] = item.value;
                }});

                method_req = $("#form-request").attr("method")
                var data = null;
                if (method_req.toUpperCase() == 'POST'){{
                   data = JSON.stringify(formData)
                }}else{{
                   data = formData
                }}

                // data = formData

                $('#frame-retorno').html("")

                $.ajax({{
                    method: method_req,
                    url: $("#form-request").attr("action"),
                    data: data,
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function(response) {{
                        console.log(response);
                        $('#frame-retorno').html(JSON.stringify(response))
                        $('#spinner-request').addClass('d-none')
                    }},
                    error: function(error) {{
                        $('#frame-retorno').html(`<p class='text-danger'>Erro de processamento. ${{error.responseText}}</p>`)
                        $('#spinner-request').addClass('d-none')
                        console.error("Erro ao enviar AJAX: ", error);
                    }}
                }});
            }});
        }});
    &lt;/script&gt;
    """
    return jsSnippet.strip()

def generateControllerSnippet(file):
    dados = getInfoRequest(file)
    controllerSnippet = f"""&lt;?php
        namespace App\Http\Controllers\ServidorApp;

        use App\Http\Controllers\Controller;
        use Illuminate\Support\Facades\DB;
        use PHPMailer\PHPMailer\PHPMailer;
        use App\Classes\\formatacoes;
        use Illuminate\Http\Request;
        use Illuminate\Support\Facades\Http;

        class {dados['nome']} extends Controller
        {{
            public function index(Request $req)
            {{
                $params = $req->all();
                $response = Http::{dados['metodo'].lower()}('{dados['dominio']}{dados['rotaApi']}',$params);
                return $response;
            }}
        }}"""
    return controllerSnippet.strip()




def generateRotaLaravelSnippet(file):
    dados = getInfoRequest(file)
    metodoSnippet = f"""
        Route::prefix('/servidorApp')->group(function () {{
            Route::{dados['metodo'].lower()}('/{dados['nome']}', 'ServidorApp\{dados['nome']}@index');
        }});"""
    return metodoSnippet.strip()
