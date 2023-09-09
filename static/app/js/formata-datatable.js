// ORDENAR TABELA BÁSICO - SOMENTE COM O SEARCH DO DATATABLE
function _datatable(idTabela, ordenaColuna, ordenaForma, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
    });
}

// ORDENA VÁRIAS TABELAS BÁSICO ATRAVÉS DO NOME DA CLASSE DA TABELA
function _datatableClasse(classe, ordenaColuna, ordenaForma, quantidadePagina = 10) {
    $('.' + classe).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        }
    });
}

// DATATABLE SEM ORDENAÇÃO
function _datatableSemOrdenação(idTabela) {
    $('#' + idTabela).DataTable({
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        }
    });
}

// DATATABLE SEM ORDENAÇÃO
function _datatableSomenteSearch(idTabela) {
    $('#' + idTabela).DataTable({
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        }
    });
}


// DATATABLE COM FILTRO EXCEL E PDF
function _datatableExcel(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'pdf',
                    text: 'Gerar PDF',
                    title: tituloPlanilha,
                },

                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

            ],
    });
}

// DATATABLE - EXPORTA SOMENTE EM EXCEL
function _datatableSoExcel(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },
            ],
    });
}

$.fn.dataTable.ext.type.order['date-br-pre'] = function ( d ) {
    var date = d.match(/(\d{2})[\/](\d{2})[\/](\d{4})/)
    return date[3]+date[2]+date[1];
};

function _datatableSoExcelComDataBR(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, colunasDeData = [], quantidadePagina = 10) {
    let columnDefs = []
    colunasDeData.forEach(colunaDeData => {
        columnDefs.push({
            "targets": colunaDeData,
            "type": 'date-br'
        });
    });

    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons": [
            {
                extend: 'excel',
                text: 'Gerar Excel',
                title: tituloPlanilha,
            },
        ],
        "columnDefs": columnDefs
    });
}

// DATATABLE - EXPORTA SOMENTE EM EXCEL E ESCOLHE COLUNAS PARA IMPRIMIR
function _datatableSoExcelEscolheColunas(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },
            ],
    });
}

// DATATABLE COM ORDENAÇÃO SEM O SEARCH - MAS COM GERAÇÃO DE EXCEL E PDF
function _datatableSemBusca(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "searching": false,

        "paging": false,

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'pdf',
                    text: 'Gerar PDF',
                    title: tituloPlanilha,
                },

                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

            ],
    });
}

// DATATABLE COM EXCEL E PDF, COM OPÇÃO DE ESCOLHA DAS COLUNAS A SEREM EXPORTADAS PRO EXCEL E PDF - PDF EM PAISAGEM
function _datatableEscolheColunas(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, quantidadePagina) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'pdf',
                    text: 'Gerar PDF',
                    orientation: 'landscape',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

            ],
    });
}

// DATATABLE COM EXCEL E PDF SEM ORDENAÇAS ASC OU DESC (SOMENTE NA ORDEM DOS INPUTS)
function _datatableBotaoSemOrdem(idTabela, tituloPlanilha, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "order": [],

        "searching": false,

        "paging": false,

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'pdf',
                    text: 'Gerar PDF',
                    title: tituloPlanilha,
                },

                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

            ],
    });
}


function _datatableAlert(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, quantidadePagina) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'pdf',
                    text: 'Gerar PDF',
                    orientation: 'landscape',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

            ],

        // "drawCallback": function( settings, total) {
        // console.log(this.fnSettings());
        // alert('Quantitade total de registros ' + this.fnSettings().fnRecordsTotal());
        // }
    });
}

//DATATABLE SEM ORDENAÇÃO
function _datatableSemPg(idTabela, tituloPlanilha, imprimeColunas) {
    $('#' + idTabela).DataTable({

        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "paging": false,
        "ordering": false,
        "info": true,
    });

}

//DATATABLE SEM ORDENAÇÃO
function _datatableSemPgSemSearch(idTabela, tituloPlanilha, imprimeColunas) {
    $('#' + idTabela).DataTable({

        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "searching": false,
        "paging": false,
        "ordering": false,
        "info": true,
    });

}

// DATATABLE SOMENTE PRA DIZER Q NÃO TEM NENHUMA INFO
function _datatableSemNada(idTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "",
            "sInfoEmpty": "",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "searching": false,
        "paging": false,
        "ordering": false,
        "info": true,
    });
}

function _datatableSemNadaSoExcel(idTabela, tituloPlanilha, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "",
            "sInfoEmpty": "",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "searching": false,
        "paging": false,
        "ordering": false,
        "info": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

            ],
    });
}

//DATATABLE COM ORDENAÇÃO POR DATA - EXPORTA EXCEL E PDF
//usar com: asset('js/portal/formata-data-datable.js')
function _datatablecomData(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, quantidadePagina) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        columnDefs: [
            {type: 'date-uk', targets: ordenaColuna}
        ],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'pdf',
                    text: 'PDF',
                    orientation: 'landscape',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

                {
                    extend: 'excel',
                    text: 'Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

            ],
    });
}

//DATATABLE COM ORDENAÇÃO POR DATA - SEM EXCEL E PDF
//usar com: asset('js/portal/formata-data-datable.js')
function _datatablecomDatasemBotao(idTabela, ordenaColuna, ordenaForma, quantidadePagina) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        columnDefs: [
            {type: 'date-uk', targets: ordenaColuna}
        ],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
    });
}

//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltros(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
        // ,

        // "footerCallback": function (row, data, start, end, display){
        //   var api = this.api();

        //   var intVal = function (i){
        //     return typeof i === 'string'?
        //     i.replace(/[\$,]/g,'')*1:
        //     typeof i === 'int'?
        //     i:0;
        //   }
        //   console.log(intVal)
        //   total = api.column(8)
        //   .data()
        //   .reduce (function (a,b) {
        //     return intVal(a) + intVal(b)
        //   }, 0)

        //   pageTotal = api
        //   .column(8, {page: 'current'})
        //   .data()
        //   .reduce(function (a,b){
        //     return intVal(a) + intVal(b)
        //   }, 0)

        //   $(api.column (8).footer()).html(
        //     '$'+pageTotal +' ( $' +total +'total)'
        //   )

        // }

    });
}

//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltrosDatas(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        columnDefs: [
            {type: 'date-uk', targets: ordenaColuna}
        ],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
        // ,

        // "footerCallback": function (row, data, start, end, display){
        //   var api = this.api();

        //   var intVal = function (i){
        //     return typeof i === 'string'?
        //     i.replace(/[\$,]/g,'')*1:
        //     typeof i === 'int'?
        //     i:0;
        //   }
        //   console.log(intVal)
        //   total = api.column(8)
        //   .data()
        //   .reduce (function (a,b) {
        //     return intVal(a) + intVal(b)
        //   }, 0)

        //   pageTotal = api
        //   .column(8, {page: 'current'})
        //   .data()
        //   .reduce(function (a,b){
        //     return intVal(a) + intVal(b)
        //   }, 0)

        //   $(api.column (8).footer()).html(
        //     '$'+pageTotal +' ( $' +total +'total)'
        //   )

        // }

    });
}

//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltrosComDataTheadPlanilha(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        columnDefs: [
            {type: 'date-uk', targets: ordenaColuna}
        ],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}

//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL - COM DATA
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltrosComDataColunaTheadPlanilha(idTabela, ordenaColuna, ordenaForma, colunaComData, tituloPlanilha, imprimeColunas, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        columnDefs: [
            {type: 'date-uk', targets: colunaComData}
        ],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}


//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltrosTheadPlanilha(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons": [
            {
                extend: 'excel',
                text: 'Gerar Excel',
                title: tituloPlanilha,
                exportOptions: {
                    columns: imprimeColunas,
                }
            },

        ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}

//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL E PDF
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltrosPDF(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

                {
                    extend: 'pdf',
                    text: 'PDF',
                    orientation: 'landscape',
                    title: tituloPlanilha,
                },
            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}

//DATATABLE COM FILTRO NA COLUNA - EXPORTA PARA EXCEL
//COLOCAR LINHA SUPERIOR NO thead DO BLADE E DEPOIS, NOMEAR OS th COM A CLASSE classTheadTabela
//colunasFiltro = COLOCAR AS COLUNAS QUE QUER COLOCAR O FILTRO DO SELECT
function _datatableFiltrosTheadPlanilhaClasse(classeTabela, ordenaColuna, ordenaForma, tituloPlanilha, imprimeColunas, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('.' + classeTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                    exportOptions: {
                        columns: imprimeColunas,
                    }
                },

            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}

// COM CLASSE
function _datatableFiltrosClassePDF(classeTabela, ordenaColuna, ordenaForma, tituloPlanilha, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('.' + classeTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },

                {
                    extend: 'pdf',
                    text: 'PDF',
                    orientation: 'landscape',
                    title: tituloPlanilha,
                },
            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}


// COM CLASSE - SÓ EXCEL SEM PDF
function _datatableFiltrosClasseExcel(classeTabela, ordenaColuna, ordenaForma, tituloPlanilha, colunasFiltro, classTheadTabela, quantidadePagina = 10) {
    $('.' + classeTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },
        // "scrollY": '50vh',
        // "scrollCollapse": true,
        "dom": 'Bfrtip',
        "buttons":
            [
                {
                    extend: 'excel',
                    text: 'Gerar Excel',
                    title: tituloPlanilha,
                },
            ],

        orderCellsTop: false,

        initComplete: function () {
            this.api().columns(colunasFiltro).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($('.' + classTheadTabela).eq(this.index()))
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        }
    });
}


//DATATABLE COM CLASSE
function _datatableClass(classeTabela, ordenaColuna, ordenaForma, quantidadePagina = 10) {
    $('.' + classeTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        }
    });
}


// DATATABLE COM BOTÕES PERSONALIZADOS
function _datatableExcelBtnPersonalizados(idTabela, ordenaColuna, ordenaForma, tituloPlanilha, quantidadePagina = 10, arrBotoesPersonalizados=[], tableTitle=null, btnExcel=true) {
    var botoes = [];
    
    if (btnExcel){
        botoes = [{
            extend: 'excel',
            text: "Exportar Excel",
            title: tituloPlanilha,
        }];
    }

    botoes = botoes.concat(arrBotoesPersonalizados);

    var domConfig = 'Bfrtip';
    if (tableTitle != null){
        domConfig = '<"row"<"col-sm-12"l>>' +
        '<"row"<"col-sm-5 text-right"B><"col-sm-4 text-center"<"table-title">><"col-sm-3 text-right"f>>'+
        '<"row"<"col-sm-12"tr>>'+
        '<"row"<"col-sm-5"i><"col-sm-7"p>>'
    }

    $('#' + idTabela).DataTable({
        "order": [[ordenaColuna, ordenaForma]],
        "pageLength": quantidadePagina,
        "language": {
            "sEmptyTable": "Nenhum registro encontrado",
            "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
            "sInfoFiltered": "(Filtrados de _MAX_ registros)",
            "sInfoPostFix": "",
            "sInfoThousands": ".",
            "sLengthMenu": "Mostrar _MENU_ resultados por página",
            "sLoadingRecords": "Carregando...",
            "sProcessing": "Processando...",
            "sZeroRecords": "Nenhum registro encontrado",
            "sSearch": "Pesquisar",
            "oPaginate": {
                "sNext": "Próximo",
                "sPrevious": "Anterior",
                "sFirst": "Primeiro",
                "sLast": "Último"
            },
            "oAria": {
                "sSortAscending": ": Ordenar colunas de forma ascendente",
                "sSortDescending": ": Ordenar colunas de forma descendente"
            }
        },

        dom: domConfig,

        "buttons": botoes,
    });

    if (tableTitle != null){
        $('.table-title').html(`<p style="text-align: center; height: 100%; width:100%; margin:0; padding:0;"><strong id="spanDataTableTitle" style="text-align: center; height: 100%; width: 100%; margin:0; padding:0;">${tableTitle}</strong></p>`);
        $('.table-title').addClass("titulo-Subprocesso");
        $('.table-title').attr("style", "border-top: solid 1px rgba(0,0,0,.3); border-bottom: solid 1px rgba(0,0,0,.3); height: 85%; width: 100%; display: flex; align-items: center; padding: 5px; color: #495057; background-color: rgba(0,0,0,.01);");
    }
    
}