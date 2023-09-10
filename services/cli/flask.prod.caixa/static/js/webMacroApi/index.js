function deletaServico(nome, metodo){
    debugger
    $('#delete-nome').text(nome)
    $('#delete-metodo').val(metodo.toLowerCase())
}

function confirmaExclusao(){
    nome = $('#delete-nome').text()
    metodo = $('#delete-metodo').val()

    dados = {nome: nome, metodo: metodo}

    data = JSON.stringify(dados)

    $.ajax({
        method: 'post',
        url: '/api/cli/delete/macroApi',
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(response) {
            console.log(response);
            msgResultado = `<i class="fa-regular fa-circle-check"></i> Serviço deletado com sucesso!`
            $("#resultado-delete").addClass('text-success')
            $("#resultado-delete").html(msgResultado)

            setInterval(() => {
                window.location.reload()
            }, 2000);
        },
        error: function(error) {
            msgResultado = error.responseText
            $("#resultado-delete").addClass('text-danger')
            $("#resultado-delete").html(msgResultado)
            console.error("Erro ao enviar AJAX: ", error);
        }
    });
}

$(document).ready(function() {
    $("#form-request").submit(function(event) {
        debugger
        event.preventDefault();

        var formData = {};

        $(this).serializeArray().forEach(function(item){
            formData[item.name] = item.value;
        });

       
        data = JSON.stringify(formData)
       
        $.ajax({
            method: 'post',
            url: $("#form-request").attr("action"),
            data: data,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                console.log(response);
                msgResultado = `<i class="fa-regular fa-circle-check"></i> Serviço criado com sucesso!`
                $("#msg-resultado-salvar").addClass('text-success')
                $("#msg-resultado-salvar").html(msgResultado)

                setInterval(() => {
                    window.location.reload()
                }, 2000);
            },
            error: function(error) {
                msgResultado = error.responseText
                $("#msg-resultado-salvar").addClass('text-danger')
                $("#msg-resultado-salvar").html(msgResultado)
                console.error("Erro ao enviar AJAX: ", error);
            }
        });
    });
});