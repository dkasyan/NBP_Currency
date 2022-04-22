#from msilib.schema import tables
import sqlite3
import random
import time
import datetime
from venv import create
import pandas as pd
import numpy as np
import sqlalchemy


class book:
    def __init__(self):
        self.dane = []

    def dodaj(self, x):
        self.dane.append(x)


logic = True


def create_table_in_book():
    conn = sqlite3.connect('example.db')
    readings = {}
    c = conn.cursor()
    counter = 0

    # CREATE TABLE[IF NOT EXISTS][schema_name].table_name(
    # column_1 data_type PRIMARY KEY,
# column_2 data_type NOT NULL,
# column_3 data_type DEFAULT 0,
# table_constraints
    # )
    c.execute("""create table if not exists readings (
        ID INTEGER PRIMARY KEY, 
	    PM25 TEXT NOT NULL,
	    PM10 TEXT NOT NULL,
        datetime TEXT NOT NULL
    );""")

    while True:
        readings = {}
        readings["PM25"] = round(random.uniform(0, 121), 1)
        readings["PM10"] = round(random.uniform(0, 201), 1)
        readings["datetime"] = time.strftime('%Y-%m-%d %H:%M:%S')

        c.execute("INSERT INTO readings VALUES (?,?,?,?)",
                  (counter, readings["datetime"], readings["PM25"], readings["PM10"]))

        conn.commit()

        counter += 1
        if counter == 100:
            break


def read_table_in_book():
    conn = sqlite3.connect('example.db')
    readings = {}
    c = conn.cursor()
    for row in c.execute('SELECT * FROM readings;'):
        print(row)
    c.close()


def read_last_ID_in_book():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    lists_timestamp = []
    list_ID = []
    list_row = []
    for row in c.execute('SELECT * FROM readings;'):
        list_row.append(row)

    last_position = list_row[-1]
    last_ID = last_position[0]
    return(last_ID)
    c.close()


while logic == False:
    print("oks")

#for row in c.execute('SELECT * FROM readings ORDER BY PM25 DESC LIMIT 10'):
#        print(row)


#def Add_New_Position(x) Funkcja dodająca coś do listy
#  Poproś o kwotę
#  Poproś o datę
#  Wstaw Kategorię
#  Dodaj Opis
# Wyswietl wpis i zapytaj czy wszystko się zgadza.
# Jeśli tak generuj unikalne ID i zapisz rekord w bazie

# def Przeglądanie to wyświetlenie kadej transakcji razem z unikalnym ID bazy danych
