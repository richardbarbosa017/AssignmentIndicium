## INTRODUÇÃO

Foi utilizado a ferramenta PowerBi para executar todas os estágios da ETL, escolhi tal ferramenta devido a familiaridade e facilidade do mesmo.

## DESENVOLVIMENTO

Como estágio inicial da ETL (extraction, transformation and loading) 
temos a extração de dados por meio do Power Query e transformação destes pelo
mesmo.


Foi utilizado a ferramenta de conversão de dados do tipo data para o formato 
brasileiro (dd/mm/yyyy), posteriormente foram excluidas as linhas em branco (neste
caso não houve resultados) e em seguida eliminado as linhas com dados considerados
inválidos (caracteres especiais) assim as linhas cujo companiesId correspondentes a 3, 8 e 22 da tabela "companies" foram
excluidas, as linhas cujo contactsId eram 3, 8 e 22 foram excluidas na tabela "contacts" e na tabela sectors
houve adaptação dos dados (sectorKey: 2 e 4 para os valores "Servicos" e "Industria"),
 pois estes eram necessários para o output, portanto não podem ser excluidos.
 
 
Realizando a analise de dados e gerando as tabelas requisitadas, podemos notar
que, devido a necessidade de exclusão de algumas linhas com dados inválidos,
há negócios realizados sem setores e contatos definidos, após uma análise mais meticulosa
(analisando os dados originais) podemos concluir que "Gage Chapman" pertence
a empresa "Auctor Foundation" pertencente ao setor 6 (Atacado), portanto, o valor
atribuido a uma suposta empresa de Id "75"(inexistente) seria atribuida a empresa
de Id "74" (Auctor Foundation) considerando que houve um erro de digitação.

Os outputs foram gerados a partir das tabelas utilizadas no PowerBi.

## DASHBOARD

Houve a produção de uma simples dashboard a fim de melhor visualizar os dados requisitados (output), para visualizar, basta instalar o PowerBi Desktop v2.83 e executar o arquivo
"ProjetoIndicium.pbix".
