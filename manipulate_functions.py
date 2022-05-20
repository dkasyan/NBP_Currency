import sqlite3

def read_table_in_book():
    conn = sqlite3.connect('example.db')
    readings = {}
    c = conn.cursor()
    for row in c.execute('SELECT * FROM readings;'):
        print(row)
    c.close()
