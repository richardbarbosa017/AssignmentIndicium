import psycopg2
import pandas as pd
import d6tstack
import glob
#Importar tabelas .tsv fornecidas
cfg_uri_psql = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'

for name in glob.glob('Inputs/*.tsv'):
    df = pd.read_csv(name,sep ="\t")
    table = name.replace('Inputs\\','')
    table = table.replace('.tsv','')
    print(table)
    d6tstack.utils.pd_to_psql(df, cfg_uri_psql, table, if_exists='replace', sep = "\t")



try:
    connection = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='postgres')

    cursor = connection.cursor()
    cursor.execute('''Delete from contacts where "contactsName" LIKE '%π%';
                        Delete from companies where "employeesName" LIKE '%π%'
    ''')
    connection.commit()
    cursor.execute('SELECT "contactsName" from contacts')
    result = cursor.fetchall()
    print (result)

except (Exception, psycopg2.Error) as error:
    print("Problema ao conectar com o Banco de dados", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexão encerrada")


