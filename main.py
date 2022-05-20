#from msilib.schema import tables
import sqlite3
import random
import time
import datetime
from venv import create
import pandas as pd
import numpy as np
import sqlalchemy

from manipulate_functions import read_table_in_book
from functions import 

users = ("Damian", "Gaba")

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
        readings["datetime"] = time.strftime('%Y-%m-%d')

        c.execute("INSERT INTO readings VALUES (?,?,?,?)",
                  (counter, readings["datetime"], readings["PM25"], readings["PM10"]))

        conn.commit()

        counter += 1
        if counter == 100:
            break


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


while logic == True:
    print("Welcome to Tip Calculator")
    decysion = int(
        input("Co chcesz wykonać \n"))
    if decysion == 1:
        print("oks")
        read_table_in_book()
    if decysion == 2:
        print("dwa")
        #TODO Add no table error handling
        create_table_in_book()

