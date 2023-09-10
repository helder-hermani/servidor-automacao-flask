function selecionaNovaMacro(event){
    $('#frameInfo').removeClass('frameInfo-show')
    select = event.currentTarget
    $("#currentMacroName").val(select.value)

    if (select.value != ""){
        statusToolBar('ready')
        // $("#btn-info").attr('disabled',false)
        // $("#btn-play").attr('disabled',false)
    }else{
        statusToolBar('idle')
        // $("#btn-info").attr('disabled',true)
        // $("#btn-play").attr('disabled',true)
        // $("#btn-pause").attr('disabled',true)
        // $("#btn-stop").attr('disabled',true)
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

function hideMacroInfo(){
    $('#frameInfo').removeClass('frameInfo-show')
}

function hideMacroHistorico(){
    $('#frameMacroHistorico').removeClass('frameInfo-show')
}

function playMacro(){
    var macroName = $("#currentMacroName").val()
    sendMensageEmulator('<hr>')
    sendMensageEmulator(`INICIALIZANDO MACRO ${macroName}`,'text-info')
    sendMensageEmulator('<hr>')

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
     
            var timer = startTrackerConnection(reqId)

            console.log(`${route}/${reqId}/${name}`)
            console.log(`${route}`)
            console.log(`${reqId}`)
            console.log(`${name}`)
            
            $.ajax({
                method: 'GET',
                url: `${route}/${reqId}/${name}/${user}`,
                success: function(response) {
                    clearInterval(timer)
                    console.log(response)
                    sendMensageEmulator(`Macro ${macroName} requisição ${reqId} finalizada!`,'text-success')
                    statusToolBar('idle')
                },
                error: function(xhr, textStatus, errorThrown) {
                    clearInterval(timer)
                    console.error(xhr.responseText);
                    sendMensageEmulator(xhr.responseText,'text-danger')
                    statusToolBar('idle')
                }
            });
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
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
                console.log(response)

                // $('#progress-bar').attr('style',`width: ${progress}%`)
                // if (progress > 100){
                //     current=0
                //     progress=0
                //     $('#progress-bar').attr('style',`width: ${progress}%`)
                //     periodo = $('#ciclo-atualizacao').val();
                // }

                if (response != null){   
                    currentStatus = $('#currentStatus').val()
                    if (currentStatus != 'idle'){
                        const {properties, mensagens, hasQuestion, hasFile, hasPassword, hasSelect, options} = response
                        console.log(response.mensagens.length)

                        if (hasQuestion){
                            question = `
                                <span>${mensagens[0]}</span>
                                <input type='text' name='answer' value='' />
                                <button type='submit' onClick='answerQuestion(event)'>Responder</button>
                                `
                            sendMensageEmulator(question);
                            $('#currentStatus').val('idle')
                        }else if (hasPassword){
                            question = `
                                <span>${mensagens[0]}</span>
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
                                <span>${mensagens[0]}</span>
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
                                <span>${mensagens[0]}</span>
                                <form enctype="multipart/form-data">
                                <input type="file" name="file" id="file-input">
                                <input type="button" value="Enviar" onclick="enviaExcel(event)">
                                </form>
                                `
                            sendMensageEmulator(question);
                            $('#currentStatus').val('idle')
                        }else{
                            // Exibe mensagens normalmente
                            mensagens.forEach(msg => {
                                sendMensageEmulator(msg)
                            });
                        }
                    }
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                clearInterval(timer)
                console.error(xhr.responseText);
                alert((xhr.responseText))
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
            
            str_options = '<option value="" selected>Macros Em execução</option>'
            active_tracks.forEach(track => {
                str_options = str_options + `<option value='${track.id}'>${track.name}</option>`
            });

            $('#macros-ativas').html(str_options)

            $('#macros-ativas').attr('onChange','habilitaRecuperaMacro(event)')
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(xhr.responseText);
            alert((xhr.responseText))
        }
    });
}

function habilitaRecuperaMacro(event){
    console.log($('#macros-ativas').val())
    reqId = event.currentTarget.value
    if ($('#macros-ativas').val() != ''){
        $('#recupera-macro-id').val(reqId)
        $('#btn-btnViewRecuperaMacro').attr('disabled',false)    
    }else{
        $('#btn-btnViewRecuperaMacro').attr('disabled',true)
    }
}

function recuperaMacro(){
    reqId = $('#recupera-macro-id').val()

    $.ajax({
    method: 'GET',
    url: `/api/tracker/getReqInfo/${reqId}`,
    success: function(response) {
        $('#frameMacroHistorico').addClass('frameInfo-show')
        const {id, name, pause, abort, broken, lastOutputIndex, outputs, input, inputPassword, question, dataframe, select, owner} = response
        str = `<p>Nome da Automação: ${name}</p>`
        str = `${str}<p>ID: ${id}</p>`
        str = `${str}<p>Proprietário: ${owner}</p>`
        str = `${str}<p>Está pausada: ${(pause == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Comando de cancelamento: ${(abort == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Parada por erro: ${(broken == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Índice da última mensagem enviada: ${lastOutputIndex}</p>`
        str = `${str}<p>Aguardando resposta de input: ${(input == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Aguardando resposta de senha: ${(inputPassword == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Aguardando arquivo Excel: ${(dataframe == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Aguardando resposta de opções: ${(select == null ? 'Não' : 'Sim')}</p>`
        str = `${str}<p>Histórico de Mensagens:</p>`
        str = str + '<div>'

        outputs.forEach(msg => {
            str = str + `<p class='p-0 m-0'>${msg}</p>`
        });

        str = str + '</div>'
        $('#frame-historico-result').html(str)
    },
    error: function(xhr, textStatus, errorThrown) {
        console.error(xhr.responseText);
        sendMensageEmulator(xhr.responseText,'text-danger')
        statusToolBar('idle')
    }
});
}

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
            $("#btn-info").attr('disabled',true)
            $("#btn-play").attr('disabled',true)
            $("#btn-pause").attr('disabled',true)
            $("#btn-stop").attr('disabled',true)
            $('#txtReqId').val('')
            $('#txtReqId').addClass('d-none')
            $('#div-periodo-atualizacao').addClass('d-none')
            // $('#atualizacao-progress').addClass('d-none')
            // $('#progress-bar').attr('style',`width: ${0}%`)
            $('#spinner-status').addClass('d-none')
            $('#sipnner-cursor').addClass('text-success')
            $('#sipnner-cursor').removeClass('text-warning')
            $('#currentStatus').val('')
            break;
        case 'ready':
            $("#btn-info").attr('disabled',false)
            $("#btn-play").attr('disabled',false)
            $("#btn-pause").attr('disabled',true)
            $("#btn-stop").attr('disabled',true)
            $('#txtReqId').val('')
            $('#txtReqId').addClass('d-none')
            $('#div-periodo-atualizacao').addClass('d-none')
            // $('#atualizacao-progress').addClass('d-none')
            // $('#progress-bar').attr('style',`width: ${0}%`)
            $('#spinner-status').addClass('d-none')
            $('#currentStatus').val('')
            break;
        case 'running':
            $("#btn-info").attr('disabled',false)
            $("#btn-play").attr('disabled',true)
            $("#btn-pause").attr('disabled',false)
            $("#btn-stop").attr('disabled',false)
            $('#txtReqId').removeClass('d-none')
            $('#div-periodo-atualizacao').removeClass('d-none')
            // $('#atualizacao-progress').removeClass('d-none')
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
