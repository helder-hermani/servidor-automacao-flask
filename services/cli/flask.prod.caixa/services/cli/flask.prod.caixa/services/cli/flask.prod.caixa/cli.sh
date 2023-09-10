#!/bin/bash
current_path="services/cli/"

if [ $# -gt 0 ]; then
    if [ "$1" == "-h" ]; then
        python services/cli/make.py -h
    elif [ "$1" == "-m" ]; then
        python $current_path"/makeMacroApi.py" $2 "\"$3"\" "\"$4"\" $5 --params "\"$6"\"
    elif [ "$1" == "-a" ]; then
        python $current_path"/makeAutomacao.py" $2 "\"$3"\" "\"$4"\"
    elif [ "$1" == "-da" ]; then
        python $current_path"/deleteAutomacao.py" $2 $3 $4
    elif [ "$1" == "-dm" ]; then
        python $current_path"/deleteMacroApi.py" $2 $3
    else
        echo "Parâmetro não reconhecido"
    fi
else
    echo -n "Comando (make ou delete): "
    read command
    if [ "$command" == "make" ]; then
        echo -n "Digite o tipo desejado (macroApi ou automacao): "
        read tipo
        if [ "$tipo" == "macroApi" ]; then
            echo -n "Nome da Macro API: "
            read nome
            echo -n "Título da aplicação: "
            read titulo
            echo -n "Descrição da aplicação: "
            read desc
            echo -n "Método da requisição (GET/POST): "
            read metodo
            echo -n 'Parâmetros da requisição (opcional, separado por virgula): '
            read params
            echo ""
            echo "--------------------------------------------------"
            echo "Iniciando construção da Macro API"
            echo "--------------------------------------------------"
            echo 
            python $current_path"/makeMacroApi.py" $nome "\"$titulo"\" "\"$desc"\" $metodo --params "\"$params"\"
        elif [ "$tipo" == "automacao" ]; then
            echo -n "Nome da Automação: "
            read nome
            echo -n "Título da automação: "
            read titulo
            echo -n "Descrição da automação: "
            read desc
            echo "--------------------------------------------------"
            echo "Iniciando construção da Automação"
            echo "--------------------------------------------------"
            python $current_path"/makeAutomacao.py" $nome "\"$titulo"\" "\"$desc"\"
        else
            echo "Tipo não reconhecido."
        fi
    elif [ "$command" == "delete" ]; then
        echo -n "Tipo de elemento (macroApi ou automacao): "
        read tipo
        if [ "$tipo" == "macroApi" ]; then
        echo -n "Nome da aplicação: "
            read nome
            echo -n "Confirme o método da requisição: "
            read metodo
            python $current_path"/deleteMacroApi.py" $nome $metodo
        elif [ "$tipo" == "automacao" ]; then
        echo -n "Nome da aplicação: "
            read nome
            echo -n "Nome da Automação a ser deletada: "
            read metodo
            python $current_path"/deleteAutomacao.py" $nome
        fi
    else
        echo "Comando não reconhecido"
    fi
fi




# python cli.py make macroApi apresentcaoMacro "Macro de apresentação à equipe" "Esta é uma macro apenas para apresentação" --method POST --params "[user, password]"
