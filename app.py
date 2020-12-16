import requests
import csv
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

def data_structure():
    with open('curency.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['currency', 'code', 'bid', 'ask'])

def outputing_data(currency, code, bid, ask):
    with open('curency.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([currency, code, bid, ask])

def count_purchases(cur, quan):
    quant = int(quan)
    for i in new_data:
        random = [i["currency"], i["code"], i["bid"], i["ask"]]
        if random[1] == cur:
            return (quant * i["ask"]) 


### Parsowanie danych z api
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()[0]
new_data = data['rates']


### Zapisywanie danych do pliku
data_structure()
for i in new_data:
    outputing_data(i["currency"], i["code"], i["bid"], i["ask"])



@app.route('/', methods=['GET', 'POST'])
def message():
    if request.method == "POST":
        datas = request.form
        currency = datas.get('currency')
        quantity = datas.get("quantity")
        ask = count_purchases(currency, quantity)
        return f'Zapłacisz {ask} zł'
        #print(currency)
        #print(quantity)

    return render_template("cc_form.html")