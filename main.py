#from msilib.schema import tables
from locale import currency
from msilib.schema import RemoveRegistry
import sqlite3
import random
import time
import datetime
from venv import create
from manipulate_functions import read_table_in_book
from check_functions import who_are_you
from check_functions import currency_checker


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
    return(last_ID +1)
    c.close()

def ask_datas_to_db():
    registration_list = ()
    registration_list.append(read_last_ID_in_book)
    registration_list.append(True)
    registration_list.append("PLN")
    registration_list.append("Damian")
    registration_list.append("Rozrywka")
    registration_list.append(-100)
    registration_list.append(time.strftime('%Y-%m-%d'))
    print(registration_list)
#    currency_answer = input("Podaj Walute PLN/USD")
#    currency_checker(currency_answer)
#    value = input("O jakiej kwocie mówimy?")


ask_datas_to_db()