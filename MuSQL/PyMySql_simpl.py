import pymysql
from contextlib import closing


def con_db():
    with closing(pymysql.connect( database="postgres", user="postgres", password="Kaliakakya", host="127.0.0.1",)) as basa:
        with basa.cursor() as cur:
            cur.execute('select * from example.db')
            print(cur.fetchall())

def main():
    con_db()

if __name__ == '__main__':
    main()
