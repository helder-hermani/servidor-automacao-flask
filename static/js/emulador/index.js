let trackerTimer;
let propertiesTimer;

function showPropriedades(){
    $('#framePropriedades').addClass('frameInfo-show')
    reqId = $("#txtReqId").val()
    propertiesTimer = setInterval(() => {
        $.ajax({
            method: 'GET',
            url: `/api/tracker/getMessages/${reqId}`,
            // url: `/api/tracker/getReqInfo/${reqId}`,
            success: function(response) {
                console.log(response)
                atualizaPropriedades(response)
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error(xhr.responseText);
                sendMensageEmulator(xhr.responseText,'text-danger')
                statusToolBar('idle')
            }
        });
    }, 3000);
}

function recuperaMacroNovo(event){
    console.log('RECUEPRANDO MACRO')
    // debugger
    reqId = event.currentTarget.value;
    const selectedIndex = event.currentTarget.selectedIndex;
    const macroName = event.currentTarget.options[selectedIndex].text;

    $('#currentStatus').val('')
    clearInterval(trackerTimer)
    limpaTela()

    $("#txtReqId").val(reqId)
    $("#currentMacroName").val(macroName)
    $('#lastMessageIndex').val(-1)

    if (event.currentTarget != ""){
        statusToolBar('running')
    }else{
        statusToolBar('idle')
    }

    sendMensageEmulator('<hr>')
    sendMensageEmulator(`RECUPERANDO MACRO ${macroName}`,'text-info')
    sendMensageEmulator('<hr>')

    $.ajax({
        method: 'GET',
        // url: `/api/tracker/getReqInfo/${reqId}`,
        url: `/api/tracker/getMessages/${reqId}`,
        success: function(response) {
            // Verificar se está pausada
            if (response.properties.pause==true){
                sendMensageEmulator('Macro PAUSADA pelo usuário. Clique para reiniciar => <button onClick="restartMacro()">Reiniciar</button>','text-warning')
                $('#sipnner-cursor').removeClass('text-success')
                $('#sipnner-cursor').addClass('text-warning')
            }

            trackerTimer = startTrackerConnection(reqId)
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            sendMensageEmulator(xhr.responseText,'text-danger')
            statusToolBar('idle')
        }
    });

    
    // $.ajax({
    //     method: 'GET',
    //     url: `/api/emulador/play/${macroName}`,
    //     success: function(response) {
    //         console.log(response)
    //         const{reqId, route, name} = response
    //         $('#txtReqId').val(reqId)
    //         user = $('#txtUser').val()

    //         statusToolBar('running')
     
            
    //     },
    //     error: function(xhr, textStatus, errorThrown) {
    //         console.error(xhr.responseText);
    //         sendMensageEmulator(xhr.responseText,'text-danger')
    //         statusToolBar('idle')
    //     }
    // });
}

function selecionaNovaMacro(event){
    $('#frameInfo').removeClass('frameInfo-show')
    select = event.currentTarget
    $("#currentMacroName").val(select.value)

    if (select.value != ""){
        statusToolBar('ready')
    }else{
        statusToolBar('idle')
    }
}

function showMacroInfo(){
    var macroName = $("#currentMacroName").val()

    $.ajax({
        method: 'GET',
        url: `/api/emulador/macroinfo/${macroName}`,
        success: function(response) {
            console.log(response)
            $('#frame-info-div-content').html(response)
            $('#frameInfo').addClass('frameInfo-show')
        },
        error: function(error) {
            console.error("Erro ao enviar AJAX: ", error);
        }
    });
}

function showLinkexterno(){
    dominio = $('#dominio').val()
    currentMacroName = $('#currentMacroName').val()
    txtUser = $('#txtUser').val()

    link = `${dominio}/emulador/externo/${currentMacroName}/${txtUser}`
    textoEvento = `window.open('${link}', 'NomeDaJanela', 'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=1200,height=600'); return false;`

    $('#a-link-externo').attr('onclick',textoEvento)
    $('#a-link-externo').text(link)

    // ="window.open('http://192.168.0.216:70/emulador/externo/minhaApp2/c084604', 'NomeDaJanela', 'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=1200,height=600'); return false;"
    $('#frameLinkExterno').addClass('frameInfo-show')
}

function hideMacroInfo(){
    $('#frameInfo').removeClass('frameInfo-show')
}

function hideLinkexterno(){
    $('#frameLinkExterno').removeClass('frameInfo-show')
}

function hidePropriedades(){
    $('#framePropriedades').removeClass('frameInfo-show')
    clearInterval(propertiesTimer)
}

function playMacro(){
    var macroName = $("#currentMacroName").val()
    sendMensageEmulator('<hr>')
    sendMensageEmulator(`INICIALIZANDO MACRO ${macroName}`,'text-info')
    sendMensageEmulator('<hr>')
    $('#lastMessageIndex').val(-1)

    $.ajax({
        method: 'GET',
        url: `/api/emulador/play/${macroName}`,
        success: function(response) {
            console.log(response)
            const{reqId, route, name} = response
            $('#txtReqId').val(reqId)
            user = $('#txtUser').val()
            // $('#currentMacroName').val(name)
            statusToolBar('running')
     
            trackerTimer = startTrackerConnection(reqId)

            console.log(`${route}/${reqId}/${name}`)
            console.log(`${route}`)
            console.log(`${reqId}`)
            console.log(`${name}`)
            
            $.ajax({
                method: 'GET',
                url: `${route}/${reqId}/${name}/${user}`,
                success: function(response) {
                    clearInterval(trackerTimer)
                    console.log(response)
                    // sendMensageEmulator(`Log de execução: ${finallog}`,'text-info');
                    atualizaPropriedades(null)
                    sendMensageEmulator(`Macro ${macroName} requisição ${reqId} finalizada!`,'text-success')
                    statusToolBar('ready')
                },
                error: function(xhr, textStatus, errorThrown) {
                    clearInterval(trackerTimer)
                    atualizaPropriedades(null)
                    console.error(xhr.responseText);
                    sendMensageEmulator(xhr.responseText,'text-danger')
                    statusToolBar('idle')
                }
            });
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            atualizaPropriedades(null)
            sendMensageEmulator(xhr.responseText,'text-danger')
            statusToolBar('idle')
        }
    });
}

function startTrackerConnection(reqId){
    console.log("iniciando timer")
    // periodo = $('#ciclo-atualizacao').val();
    current = 0;
    intervalId = setInterval(() => {
        // current += 1;
        // progress = (current/periodo)*100
        $.ajax({
            method: 'GET',
            url: `/api/tracker/getMessages/${reqId}`,
            success: function(response) {
                try {
                    console.log(response)
                    const {properties, outputs, historico, hasQuestion, hasFile, hasPassword, hasSelect, options, lastOutputIndex, finallog} = response
                    atualizaPropriedades(response)
                    // console.log(historico)

                    if (properties != null){   
                        currentStatus = $('#currentStatus').val()
                        if (currentStatus != 'idle'){
                            if (properties.pause == true){
                                sendMensageEmulator('Macro PAUSADA pelo usuário. Clique para reiniciar => <button onClick="restartMacro()">Reiniciar</button>','text-warning')
                                $('#sipnner-cursor').removeClass('text-success')
                                $('#sipnner-cursor').addClass('text-warning')
                                $('#currentStatus').val('idle')
                            }else if (hasQuestion){
                                question = `
                                    <span>${outputs[0]}</span>
                                    <input type='text' name='answer' value='' />
                                    <button type='submit' onClick='answerQuestion(event)'>Responder</button>
                                    `
                                sendMensageEmulator(question);
                                $('#currentStatus').val('idle')
                            }else if (hasPassword){
                                question = `
                                    <span>${outputs[0]}</span>
                                    <input type='password' name='answer' value='' />
                                    <button type='submit' onClick='answerQuestionPassword(event)'>Responder</button>
                                    `
                                console.log(question)
                                sendMensageEmulator(question);
                                $('#currentStatus').val('idle')
                            }else if (hasSelect){
                                str_options = ''
                                options.forEach(option => {
                                    str_options = str_options + `<option value='${option}'>${option}</option>`
                                });
                                question = `
                                    <span>${outputs[0]}</span>
                                    <select name='answer'>
                                    ${str_options}
                                    </select>
                                    <button type='submit' onClick='answerSelect(event)'>Responder</button>
                                    `
                                console.log(question)
                                sendMensageEmulator(question);
                                $('#currentStatus').val('idle')
                            }else if (hasFile){
                                question = `
                                    <span>${outputs[0]}</span>
                                    <form enctype="multipart/form-data">
                                    <input type="file" name="file" id="file-input">
                                    <input type="button" value="Enviar" onclick="enviaExcel(event)">
                                    </form>
                                    `
                                sendMensageEmulator(question);
                                $('#currentStatus').val('idle')
                            }else{
                                // Exibe mensagens normalmente
                                lastMessageIndex = parseInt($('#lastMessageIndex').val())
                                var novasMsg = historico.filter(function(elemento, indice) {
                                    return indice > lastMessageIndex;
                                });

                                novasMsg.forEach(msg => {
                                    lastMessageIndex=lastMessageIndex+1
                                    sendMensageEmulator(msg)
                                });

                                $('#lastMessageIndex').val(lastMessageIndex)
                                // outputs.forEach(msg => {
                                //     sendMensageEmulator(msg)
                                // });
                                // $('#currentStatus').val('')
                            }
                        }else{
                            if ((properties.pause)
                                || (hasQuestion)
                                || (hasPassword)
                                || (hasSelect)
                                || (hasFile)){
                                    $('#currentStatus').val('idle')
                                }else{
                                    $telaEmulador = document.getElementById('telaEmulador')
                                    $ultimaMsg = $telaEmulador.lastElementChild
                                    $ultimaMsg.innerHTML = '<p style="color: gray;">Interação efetuada por outro usuário.</p>'
                                    $('#currentStatus').val('')
                                    $('#sipnner-cursor').addClass('text-success')
                                    $('#sipnner-cursor').removeClass('text-warning')
                                }
                        }
                        //Verifica se ainda permanece o motivo do idle
                    }else{
                        sendMensageEmulator('Requisição não existe na fila','text-danger');
                        sendMensageEmulator(`Log de execução: ${finallog}`,'text-info');
                        atualizaPropriedades(null)
                        statusToolBar('idle')
                        $('#currentStatus').val('')
                        clearInterval(trackerTimer)
                    }
                }catch(error){
                    sendMensageEmulator(error);
                    $('#currentStatus').val('')
                    clearInterval(trackerTimer)
                    atualizaPropriedades(null)
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                // clearInterval(timer)
                sendMensageEmulator(xhr.responseText, 'text-danger');
                $('#currentStatus').val('')
                atualizaPropriedades(null)
                clearInterval(trackerTimer)
                console.log(xhr.responseText);
                // console.error(xhr.responseText);
                // alert((xhr.responseText))
            }
        });

    }, 5000);

    return intervalId
}


function stopMacro(){
    var reqId = $('#txtReqId').val()
    var user = $('#txtUser').val()
    $.ajax({
        method: 'GET',
        url: `/api/emulador/stop/${reqId}/${user}`,
        success: function(response) {
            console.log(response)
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

function pauseMacro(){
    var reqId = $('#txtReqId').val()
    var user = $('#txtUser').val()

    $.ajax({
        method: 'GET',
        url: `/api/emulador/pause/${reqId}/${user}`,
        success: function(response) {
            console.log(response)
            sendMensageEmulator('Macro PAUSADA pelo usuário. Clique para reiniciar => <button onClick="restartMacro()">Reiniciar</button>','text-warning')
            $('#sipnner-cursor').removeClass('text-success')
            $('#sipnner-cursor').addClass('text-warning')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

function restartMacro(){
    var reqId = $('#txtReqId').val()

    $.ajax({
        method: 'GET',
        url: `/api/emulador/restart/${reqId}`,
        success: function(response) {
            console.log(response)
            sendMensageEmulator('Macro REINICIADA.','text-warning')
            $('#sipnner-cursor').addClass('text-success')
            $('#sipnner-cursor').removeClass('text-warning')
            $('#currentStatus').val('')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

function limpaTela(){
    $('#telaEmulador').html('');
}

function refreshMacrosExecucao(){
    $.ajax({
        method: 'GET',
        url: `/api/tracker/gettracks`,
        success: function(response) {
            console.log(response)
            active_tracks = JSON.parse(response)
            console.log(active_tracks)
            debugger;
            
            str_options = '<option value="" selected>Macros Em execução</option>'
            active_tracks.forEach(track => {
                str_options = str_options + `<option value='${track.id}'>${track.name}</option>`
            });

            $('#macros-ativas').html(str_options)

            $('#macros-ativas').attr('onChange','recuperaMacroNovo(event)')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

// function habilitarecuperaMacro(event){
//     console.log($('#macros-ativas').val())
//     reqId = event.currentTarget.value
//     if ($('#macros-ativas').val() != ''){
//         $('#recupera-macro-id').val(reqId)
//         $('#btn-btnViewrecuperaMacro').attr('disabled',false)    
//     }else{
//         $('#btn-btnViewRecuperaMacro').attr('disabled',true)
//     }
// }

// function recuperaMacro(){
//     reqId = $('#recupera-macro-id').val()

//     $.ajax({
//     method: 'GET',
//     url: `/api/tracker/getReqInfo/${reqId}`,
//     success: function(response) {
//         $('#frameMacroHistorico').addClass('frameInfo-show')
//         const {id, name, pause, abort, broken, lastOutputIndex, outputs, input, inputPassword, question, dataframe, select, owner} = response
//         str = `<p>Nome da Automação: ${name}</p>`
//         str = `${str}<p>ID: ${id}</p>`
//         str = `${str}<p>Proprietário: ${owner}</p>`
//         str = `${str}<p>Está pausada: ${(pause == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Comando de cancelamento: ${(abort == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Parada por erro: ${(broken == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Índice da última mensagem enviada: ${lastOutputIndex}</p>`
//         str = `${str}<p>Aguardando resposta de input: ${(input == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Aguardando resposta de senha: ${(inputPassword == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Aguardando arquivo Excel: ${(dataframe == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Aguardando resposta de opções: ${(select == null ? 'Não' : 'Sim')}</p>`
//         str = `${str}<p>Histórico de Mensagens:</p>`
//         str = str + '<div>'

//         outputs.forEach(msg => {
//             str = str + `<p class='p-0 m-0'>${msg}</p>`
//         });

//         str = str + '</div>'
//         $('#frame-historico-result').html(str)
//     },
//     error: function(xhr, textStatus, errorThrown) {
//         console.error(xhr.responseText);
//         sendMensageEmulator(xhr.responseText,'text-danger')
//         statusToolBar('idle')
//     }
// });
// }

// function recuperaMacrorecuperaMacro(event){
//     const macroName = event.currentTarget.value
//     $("#currentMacroName").val(macroName)

//     $.ajax({
//         method: 'GET',
//         url: `/api/emulador/play/${macroName}`,
//         success: function(response) {
//             console.log(response)
//             const{reqId, route, name} = response
//             $('#txtReqId').val(reqId)
//             statusToolBar('running')
     
//             var timer = startTrackerConnection(reqId)
            
//         },
//         error: function(xhr, textStatus, errorThrown) {
//             console.error(xhr.responseText);
//             sendMensageEmulator(xhr.responseText,'text-danger')
//             statusToolBar('idle')
//         }
//     });
// }

function answerQuestion(event){
    var reqId = $('#txtReqId').val()
    $btn = event.currentTarget
    answer = $btn.previousElementSibling.value

    $.ajax({
        method: 'GET',
        url: `/api/tracker/answerInput/${reqId}/${answer}`,
        success: function(response) {
            console.log(response)
            sendMensageEmulator(response.mensagens,'text-warning')
            $('#currentStatus').val('')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

function answerQuestionPassword(event){
    var reqId = $('#txtReqId').val()
    $btn = event.currentTarget
    answer = $btn.previousElementSibling.value

    $.ajax({
        method: 'GET',
        url: `/api/tracker/answerInputPassword/${reqId}/${answer}`,
        success: function(response) {
            console.log(response)
            sendMensageEmulator(response.mensagens,'text-warning')
            $('#currentStatus').val('')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

function answerSelect(event){
    var reqId = $('#txtReqId').val()
    $btn = event.currentTarget
    answer = $btn.previousElementSibling.value

    $.ajax({
        method: 'GET',
        url: `/api/tracker/answerSelect/${reqId}/${answer}`,
        success: function(response) {
            console.log(response)
            sendMensageEmulator(response.mensagens,'text-warning')
            $('#currentStatus').val('')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}


function sendMensageEmulator(msg, style=null){
    if (style == null){
        style='text-light'
    }
    $telaEmulador = document.getElementById('telaEmulador')
    $linhaMsg = document.createElement('p')
    $linhaMsg.innerHTML = `${msg}`
    $linhaMsg.classList.add(style)
    $telaEmulador.appendChild($linhaMsg)

    const alturaTotal = $telaEmulador.scrollHeight;
    const alturaVisivel = $telaEmulador.clientHeight;
    const rolagemMaxima = alturaTotal - alturaVisivel;

    $telaEmulador.scrollTop = rolagemMaxima;
}

function statusToolBar(status){
    switch (status) {
        case 'idle':
            $("#btn-nova").attr('disabled',true)
            $("#btn-excluir").attr('disabled',true)
            $("#btn-info").attr('disabled',true)
            $("#btn-link-externo").attr('disabled',true)
            $("#btn-play").attr('disabled',true)
            $("#btn-pause").attr('disabled',true)
            $("#btn-stop").attr('disabled',true)
            $("#btn-reqInfo").attr('disabled',true)
            $('#txtReqId').val('')
            $('#txtReqId').addClass('d-none')
            $('#div-periodo-atualizacao').addClass('d-none')
            $('#spinner-status').addClass('d-none')
            $('#sipnner-cursor').addClass('text-success')
            $('#sipnner-cursor').removeClass('text-warning')
            $('#currentStatus').val('')
            break;
        case 'ready':
            $("#btn-nova").attr('disabled',false)
            $("#btn-excluir").attr('disabled',false)
            $("#btn-info").attr('disabled',false)
            $("#btn-link-externo").attr('disabled',false)
            $("#btn-play").attr('disabled',false)
            $("#btn-pause").attr('disabled',true)
            $("#btn-stop").attr('disabled',true)
            $("#btn-reqInfo").attr('disabled',true)
            $('#txtReqId').val('')
            $('#txtReqId').addClass('d-none')
            $('#div-periodo-atualizacao').addClass('d-none')
            $('#spinner-status').addClass('d-none')
            $('#currentStatus').val('')
            break;
        case 'running':
            $("#btn-nova").attr('disabled',true)
            $("#btn-excluir").attr('disabled',true)
            $("#btn-info").attr('disabled',false)
            $("#btn-link-externo").attr('disabled',false)
            $("#btn-play").attr('disabled',true)
            $("#btn-pause").attr('disabled',false)
            $("#btn-stop").attr('disabled',false)
            $("#btn-reqInfo").attr('disabled',false)
            $('#txtReqId').removeClass('d-none')
            $('#div-periodo-atualizacao').removeClass('d-none')
            $('#spinner-status').removeClass('d-none')
            break;
        default:
            break;
    }
}

function enviaExcel(event){
    $btn = event.currentTarget
    $arquivo = $btn.previousElementSibling
    // $arquivo = document.getElementById('file-input')
    const arquivo = $arquivo.files[0];

    const formData = new FormData();
    formData.append('file', arquivo);

    var reqId = $('#txtReqId').val()

    $.ajax({
        type: 'POST',
        url: `/api/emulador/upload_excel/${reqId}`,
        data: formData,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log(response);
            // alert('Arquivo Excel enviado com sucesso!');
            sendMensageEmulator(response.mensagens,'text-warning')
            $('#currentStatus').val('')
        },
        error: function (error) {
            console.error(error);
            alert('Erro ao enviar o arquivo Excel.');
            $('#currentStatus').val('')
        }
    });
};


function atualizaPropriedades(dadosReq){
    console.log(dadosReq)
    
    if (dadosReq != null){
        var {properties, outputs, historico, hasQuestion, hasFile, hasPassword, hasSelect, options, lastOutputIndex} = dadosReq
        if (properties != null){
            autStatus = 'ATIVO'
            id = properties.id
            macroName = properties.name
            owner = properties.owner
            starttime = properties.starttime
            lastuser = properties.lastuser
            properties.pause==true ? pause='<strong>Sim</strong>' : pause = 'Não'
            properties.abort==true ? abort='<strong>Sim</strong>' : abort = 'Não'
            hasQuestion == true ? question='<strong>Sim</strong>' : question = 'Não'
            hasPassword == true ? inputPassword='<strong>Sim</strong>' : inputPassword = 'Não'
            hasSelect == true ? select='<strong>Sim</strong>' : select = 'Não'
            hasFile == true ? excel='<strong>Sim</strong>' : excel = 'Não'
            // dataframe==null ? dataframe='Não' : dataframe = 'Sim'
    
            $('#prop-status').html(autStatus)
            $('#prop-id').html(id)
            $('#prop-Nome').html(macroName)
            $('#prop-proprietario').html(owner)
            $('#prop-inicio').html(starttime)
            $('#prop-last-user').html(lastuser)
            $('#prop-pausada').html(pause)
            $('#prop-cancelamento').html(abort)
            $('#prop-iUltimaMsg').html(lastOutputIndex)
            $('#prop-input').html(question)
            $('#prop-password').html(inputPassword)
            $('#prop-select').html(select)
            $('#prop-excel').html(excel)
        }else{
            $('#prop-status').text('INATIVO')
            $('#prop-id').text('')
            $('#prop-Nome').text('')
            $('#prop-proprietario').text('')
            $('#prop-inicio').text('')
            $('#prop-last-user').text('')
            $('#prop-pausada').text('')
            $('#prop-cancelamento').text('')
            $('#prop-iUltimaMsg').text('')
            $('#prop-input').text('')
            $('#prop-password').text('')
            $('#prop-select').text('')
            $('#prop-excel').text('')
        }
    }else{
        $('#prop-status').text('INATIVO')
        $('#prop-id').text('')
        $('#prop-Nome').text('')
        $('#prop-proprietario').text('')
        $('#prop-inicio').text('')
        $('#prop-last-user').text('')
        $('#prop-pausada').text('')
        $('#prop-cancelamento').text('')
        $('#prop-iUltimaMsg').text('')
        $('#prop-input').text('')
        $('#prop-password').text('')
        $('#prop-select').text('')
        $('#prop-excel').text('')
    }    
}

function criaNovaAutomacao(){
    telaCadastro = `
    <div style='padding: 2rem;'>
        <hr>
        <p class='text-info'>Registro de nova automação</p>
        <hr>
        <div class="row mb-1">
            <div class="col-3">
                Nome de Automação:
            </div>
            <div class="col-3">
                <input type="text" id="make-nome" style="width: 100%;" placeholder="Nome, sem espaços"/>
            </div>
        </div>
        <div class="row mb-1">
            <div class="col-3">
                Título de Automação:
            </div>
            <div class="col-3">
                <input type="text" id="make-titulo" style="width: 100%;"/>
            </div>
        </div>
        <div class="row mb-1">
            <div class="col-3">
                Descrição:
            </div>
            <div class="col-3">
            <input type="text" id="make-desc" style="width: 100%;"/>
            </div>
        </div>
        <div class="row mb-1">
            <div class="col-3">
            </div>
            <div class="col-3">
                <button class="btn btn-dark" style="width: 100%;" onClick='salvaNovaAutomacao()'>Salvar</button>
            </div>
        </div>
        <div class="row mb-1">
            <div class="col-3">
            </div>
            <div class="col-3">
                <p id="msg-resultado"></p>
            </div>
        </div>
    </div>
    `
    $('#telaEmulador').html('')
    $('#telaEmulador').html(telaCadastro)
}

function salvaNovaAutomacao(){
    nome = document.getElementById('make-nome').value
    titulo = document.getElementById('make-titulo').value
    desc = document.getElementById('make-desc').value
    
    dados = {nome: nome, titulo: titulo, desc: desc}

    data = JSON.stringify(dados)

    $.ajax({
        method: 'post',
        url: '/api/cli/make/automacao',
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(response) {
            console.log(response);
            msgResultado = `<i class="fa-regular fa-circle-check"></i> Serviço criado com sucesso!`
            $resultado = document.getElementById('msg-resultado')
            $resultado.classList.add('text-success')
            $resultado.innerHTML = msgResultado

            setInterval(() => {
                window.location.reload()
            }, 2000);
        },
        error: function(error) {
            msgResultado = error.responseText
            $resultado = document.getElementById('msg-resultado')
            $resultado.classList.add('text-danger')
            $resultado.innerHTML(msgResultado)
            console.error("Erro ao enviar AJAX: ", error);
        }
    });
}

function deletaAutomacao(){
    nome = $('#currentMacroName').val()
    telaCadastro = `
    <div style='padding: 2rem;'>
        <p>Confirma a exclusão da automação <span id="delete-nome">${nome}</span>?</p>
        <p>Este processo é irreversível.</p>
        <button class="btn btn-danger" style="width: 10%;" onClick='confirmaDeleteAutomacao("${nome}")'>Confirmar</button>
        <div id="delete-resultado"></div>
    </div>
    `
    $('#telaEmulador').html('')
    $('#telaEmulador').html(telaCadastro)
}

function confirmaDeleteAutomacao(nome){
    dados = {nome: nome}

    data = JSON.stringify(dados)

    $.ajax({
        method: 'post',
        url: '/api/cli/delete/automacao',
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(response) {
            console.log(response);
            msgResultado = `<i class="fa-regular fa-circle-check"></i> Automação deletada com sucesso!`
            $resultado = document.getElementById('delete-resultado')
            $resultado.classList.add('text-success')
            $resultado.innerHTML = msgResultado

            setInterval(() => {
                window.location.reload()
            }, 2000);
        },
        error: function(error) {
            msgResultado = error.responseText
            $resultado = document.getElementById('delete-resultado')
            $resultado.classList.add('text-danger')
            $resultado.innerHTML(msgResultado)
            console.error("Erro ao enviar AJAX: ", error);
        }
    });
}