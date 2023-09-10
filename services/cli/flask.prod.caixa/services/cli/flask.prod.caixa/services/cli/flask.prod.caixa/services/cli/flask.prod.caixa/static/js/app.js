function make_test(){
    alert('Teste realizado com sucesso!')
}

function makeAjax(url,method,data=null,successFunc,errorFunc,headers=null,dataType='application/json; charset=utf-8'){
    console.log(url)
    console.log(method)
    console.log(data)
    console.log(dataType)

    if (dataType.indexOf('json') >= 0){
        data = JSON.stringify(data)
    }

    $.ajax({
        url: url,
        method: method,
        contentType: dataType,
        // headers: headers,
        data: data,
        success: function (resultado){
            successFunc()
        },
        error: function(x,y,z){
            errorFunc()
        }
    });
}