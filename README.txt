
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
há negocios realizados sem setores definido, após uma análise mais meticolosa
(analisando os dados originais) podemos concluir que "Gage Chapman" pertence
a empresa "Auctor Foundation" pertencente ao setor 6 (Atacado), portanto, o valor
atribuido a uma suposta empresa de Id "75"(inexistente) seria atribuida a empresa
de Id "74" (Auctor Foundation) considerando que houve um erro de digitação.