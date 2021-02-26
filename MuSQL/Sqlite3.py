import sqlite3
def connect():
    con = sqlite3.connect("mudatabase.db")
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE if not exists albums 
                    (title text, artist text, release_data text,
                    pyblisher text, media_type text)
                    ''')
    # Вставляем данные в таблицу
    # cursor.execute("""INSERT INTO albums
    #                   VALUES (
    #                   'Glow', 'Andy Hunter', '7/24/2012',
    #                   'Xplore Records', 'MP3')""")
    # con.commit()
    #
    # # Вставляем множество данных в таблицу используя безопасный метод "?"
    # albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
    #           ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
    #           ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
    #           ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
    #
    # cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
    # con.commit()

    # sql = """ UPDATE albums SET artist = 'John Doe'
    # WHERE artist = 'Andy Hunter'"""
    #
    # cursor.execute(sql)


    sql = 'DELETE FROM albums WHERE artist = "John Doe"'
    cursor.execute(sql)
    cursor.execute("SELECT * FROM albums ")
    resalt = cursor.fetchall()
    for cur in resalt:
        print(cur)
    cursor.close()
    con.close()


def main():
    connect()
if __name__ == '__main__':
    main()
