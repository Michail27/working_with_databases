# import sqlite3
# conn = sqlite3.connect("student.db")
#
# cursor = conn.cursor()
#
# # cursor.execute("CREATE TABLE students(First_name TEXT, Last_name TEXT, Age INTEGER);")
# # cursor.execute("INSERT INTO students VALUES('Jems', 'Blec', 18);" )
# cursor.execute("SELECT * FROM students;")
# results = cursor.fetchone()
# for i in results:
#     print(i)
# conn.commit()
#
# conn.close()



import sqlite3


def fib(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS fib (
                            calculated_value INTEGER)''')
    cursor.executemany('INSERT INTO fib VALUES (?)',
                       [(str(x),) for x in fib(15)])


cursor.execute('SELECT * FROM fib')
print(cursor.fetchall())

connection.close()