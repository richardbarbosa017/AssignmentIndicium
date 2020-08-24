## INTRODUÇÃO

Optei por realizar o projeto com a linguagem de programação Python e o PostgreSQL, durante a execução criei um banco de dados em servidor local por meio do PgAdmin4 (localhost, port:5432), a partir da criação realizei um codigo em python para importação dos arquivos ".tsv" para o servidor e, posteriormente, execução de scripts SQL por meio do "execute" no python (para selecionar os dados segundo as tarefas requisitadas).
Foi utilizado a ferramenta PowerBi para executar todas os estágios da ETL de maneira alternativa ao desenvolvido em Python e SQL, escolhi tal ferramenta devido a familiaridade e facilidade do mesmo.

## DESENVOLVIMENTO PYTHON/SQL

Inicialmente é necessário a criação de um banco de dados em um servidor local, utilizei o PostgreSQL para tal tarefa, é necessário iniciar o PgAdmin4, setar o usuário e senha e está pronto o servidor de preferencia setar igual ao meu para não haver problemas: "usuario:postgres, senha:postgres e database: postgres" (guarde o nome de usuario, senha e nome da database criada/utilizada no servidor).
Como salientado na introdução a importação de dados e conexão com o banco de dados foi realizada via python, algumas bibliotecas necessitam ser instaladas para a execução do programa:
psycopg2
pandas as pd
d6tstack
glob
csv
Toda a parte de conexão com o servidor ficou com a biblioteca Psycopg2, pandas com a parte de abertura e leitura do arquivo tsv, d6tstack com a parte de escrever o dataframe e esta necessita de uma uri de configuração o padrão para setar é "cfg_uri_psql = 'postgresql+psycopg2://user:password@localhost/database' ".
As tarefas foram realizadas utilizando codigo SQL disponibilizadas de maneira separas no arquivo Transform.sql.
A execução do arquivo main.py gera os outputs pedidos em forma de csv (out 1,out 2 e out 3).
O out 1 refere-se ao valor vendido por contato, out 2 ao valor vendido por mês e out 3 a porcentagem vendida por setor.

## DESENVOLVIMENTO POWERBI

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

![alt text](https://github.com/richardbarbosa017/AssignmentIndicium/blob/master/Dashboard.PNG)
