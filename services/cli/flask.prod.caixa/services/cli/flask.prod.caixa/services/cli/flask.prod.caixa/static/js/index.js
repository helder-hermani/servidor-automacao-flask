function gerarHash() {
    var caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789';
    var hash = '';
  
    for (var i = 0; i < 6; i++) {
      var randomIndex = Math.floor(Math.random() * caracteres.length);
      hash += caracteres.charAt(randomIndex);
    }
  
    return hash;
  }

function make_request(url, id_req){
    const settings = {
        async: true,
        crossDomain: true,
        url: `${url}${id_req}`,
        method: 'GET'
    };
    
    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function iniciar_macro(macro_name){
    id_req = gerarHash()
    document.getElementById('id_req').value = id_req
    make_request(`/macro/${macro_name}/`,id_req)

    const refresh = setInterval(() => {
        get_tracker(refresh)
    }, 5000);
}

function get_tracker(interval){
    track_id = document.getElementById('id_req').value
    var resolve = null
    const settings = {
        async: true,
        crossDomain: true,
        url: `/api/gettrack/${track_id}`,
        method: 'GET'
    };
    
    $.ajax(settings).done(function (response) {
        console.log(response.length);
        if (response.length==undefined){
            clearInterval(interval)
        }
    });

}