#from msilib.schema import tables
from locale import currency
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
    return(last_ID)
    c.close()

def ask_datas_to_db():
    registration_list = ()
    currency_answer = input("Podaj Walute PLN/USD")
    currency_checker(currency_answer)
    value = input("O jakiej kwocie mówimy?")
    valu_checker(value) 

#    tag = input("Jaki tag")
#    date = input("Podaj date")


def script_menu():
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

ask_datas_to_db()