function enableDeploy(){
    $('#btn-inicia-backup').attr('disabled', false)
}

function iniciaDeploy(){
    $('#nome-servidor-destino-backup').text($('#servidor-destino').val())
    $('#nome-servidor-destino-transferencia').text($('#servidor-destino').val())
    $('#disabled-cover').removeClass('d-none')
    iniciaBackup()
}

function iniciaBackup(){
    $('#linha-backup').removeClass('d-none')
    $.ajax({
        method: 'GET',
        url: `/api/deploy/backup/${$('#servidor-destino').val()}`,
        success: function(response) {
            console.log(response)
            $('#txt-resultado-deploy').text(response.status)
            $('#txt-resultado-deploy').addClass('text-success')
            iniciaTransDestino()
        },
        error: function(xhr, textStatus, errorThrown) {
            $('#txt-resultado-deploy').text(xhr.responseText)
            $('#txt-resultado-deploy').addClass('text-danger')
            $('#disabled-cover').addClass('d-none')
            console.log("Erro ao enviar AJAX: ", xhr.responseText);
        }
    });
}

function iniciaTransDestino(){
    $('#linha-transf').removeClass('d-none')

    var isChecked = $("#deploy-ignore").prop("checked");

    use_ignore = 0
    if (isChecked){
        use_ignore = 1
    }

    $.ajax({
        method: 'GET',
        url: `/api/deploy/transferencia/${$('#servidor-destino').val()}/${use_ignore}`,
        success: function(response) {
            console.log(response)
            $('#txt-resultado-deploy').text(response.status)
            $('#txt-resultado-deploy').addClass('text-success')
            $('#disabled-cover').addClass('d-none')
        },
        error: function(xhr, textStatus, errorThrown) {
            $('#txt-resultado-deploy').text(xhr.responseText)
            $('#txt-resultado-deploy').addClass('text-danger')
            console.log("Erro ao enviar AJAX: ", xhr.responseText);
            $('#disabled-cover').addClass('d-none')
        }
    });
}
