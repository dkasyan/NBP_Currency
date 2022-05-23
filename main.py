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
from check_functions import who_are_you

users = ("Damian", "Gaba")

class book:
    def __init__(self):
        self.dane = []

    def dodaj(self, x):
        self.dane.append(x)


logic = True





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

