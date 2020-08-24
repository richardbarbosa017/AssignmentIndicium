import psycopg2
import pandas as pd
import d6tstack
import glob
import csv
#Importar tabelas .tsv fornecidas
cfg_uri_psql = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'

for name in glob.glob('Inputs/*.tsv'):
    df = pd.read_csv(name,sep ="\t")
    table = name.replace('Inputs\\','')
    table = table.replace('.tsv','')
    d6tstack.utils.pd_to_psql(df, cfg_uri_psql, table, if_exists='replace', sep = "\t")

try:
    connection = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='postgres')
    #Extracao de valores invalidos
    cursor = connection.cursor()
    cursor.execute('''Delete from contacts where "contactsName" LIKE '%π%';
                        Delete from companies where "employeesName" LIKE '%π%'
    ''')
    connection.commit()
    #Task 1
    cursor.execute('''SELECT deals."contactsId" , contacts."contactsName", sum ("dealsPrice")
                    from deals, contacts
                    where deals."contactsId" = contacts." contactsId"
                    group by deals."contactsId",contacts."contactsName"
                    order by deals."contactsId"''')
    result = cursor.fetchall()
    #escreve resultados em arquivo csv
    with open("out1.csv", "w", newline='') as csv_file: 
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(result)

    #Task 2
    cursor.execute('''SELECT cast(extract(month from (TO_DATE("dealsDateCreated", 'MM/DD/YYYY'))) as integer) as monthid , TO_CHAR(TO_DATE("dealsDateCreated", 'MM/DD/YYYY'), 'Month') AS "Month",sum("dealsPrice")
                        from deals
                        group by "Month", monthid
                        order by monthid
    ''')
    result = cursor.fetchall()
    #escreve resultados em arquivo csv
    with open("out2.csv", "w", newline='') as csv_file: 
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(result)

    #Task 3
    cursor.execute('''select ca."sector",round(sum ("dealsPrice")/(select sum("dealsPrice") from deals),3) as porcentagem
                        from deals join (select co."companiesId", "sector"
                                        from companies as co join sectors as se on co."sectorKey"=se."sectorKey") as ca on deals."companiesId"=ca."companiesId"
                        group by ca."sector"
                        order by porcentagem desc
    ''')
    result = cursor.fetchall()
    #escreve resultados em arquivo csv
    with open("out3.csv", "w", newline='') as csv_file: 
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(result)


except (Exception, psycopg2.Error) as error:
    print("Problema ao conectar com o Banco de dados", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexão encerrada")


