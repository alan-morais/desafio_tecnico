# conexão com o postgres
import json
import psycopg2
try:
    con = psycopg2.connect(host='localhost', database='imdb',
                       user='postgres', password='1234')
    cur = con.cursor()
    cur.execute('SELECT ano, titulo	FROM public.filmes_1900;')

    # cur.execute('SELECT todas_as_tabelas FROM public.tabelas;')

    rec = cur.fetchall()
    minhaTupla = rec
    print('banco',rec,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Erro ao conectar ao PostgreSQL", error)
finally:
    #fechando conexão
    if(con):
        cur.close()
        con.close()
        print("conexão com o PostgreSQL fechada")

jsonStr = json.dumps(minhaTupla, sort_keys=True)
jsonArr = json.loads(jsonStr)
with open('dados.json', 'w') as json_file:
    json.dump(jsonArr, json_file, indent=4,separators=(",", " : ",))
