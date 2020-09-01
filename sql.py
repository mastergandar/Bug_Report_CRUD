import psycopg2 as sql_work

database = '***'
user = '***'
password = '***'
host = '***'

try:
    conn = sql_work.connect(dbname = database, user = user, password = password, host = host)
    curs = conn.cursor()
except:
    print('Connection error, check your internet connection and try more.')
    #finally:
     #   cursor.close()
     #   conn.close()
