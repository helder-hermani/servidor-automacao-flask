<!-- -*- coding: utf-8 -*- -->

##### Nome
consultaSinafWeb
<br>

##### Titulo
Consulta Dle SinafWeb
<br>

##### Descrição
Consulta número e situação do DLE no SINAFWEB para uma determinada proposta do SIMOV.
<br>

##### Instruções
Informe a unidade da proposta (sem DV), o número da unidade (440...), o nome do proponente (conforme SIMOV, considerando inclusive acentos e abreviações), o valor do DLE (sem separador de milhar e com '.' como separador decimal) e a data da proposta (formato dd/mm/yyyy).
<br>

##### Bibliotecas de Terceiros
- Nenhuma
<br>

##### Entidades Banco de Dados
- Nenhuma
<br>

##### Rota View (apenas para esta documentação)
- /web/macroapi/viewMacro
<br>

##### Rota API
- /macroapi/consultaSinafWeb
<br>

##### Método Http
- POST
<br>

##### Parâmetros
- user
- password
- unidadeMovimento
- conciliacao
- nomeProponente
- valorRP
- dataProposta
