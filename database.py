import sqlite3

def createdb(data):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

# Создание таблицы
    cursor.execute("""CREATE TABLE test
                (date INTEGER , name text, company text,
                adres text, name_object text, quantity real,
                price real, sum real, discount real, end_sum real,
                type_work text, comment text)""")
    cursor.executemany("INSERT INTO test VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", data)


    conn.commit()
    return cursor

def deletetable(cursor):
    cursor.execute("""" DROP TABLE test """)
    
    
