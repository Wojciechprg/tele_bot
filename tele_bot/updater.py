from pymongo import MongoClient
from datetime import date

client = MongoClient("mongodb://127.0.0.1:27017")
database = client.sbd
collection = database['update']

today = date.today()

#collection.insert_one({'data': '04.11.2021'})
data=collection.distinct("data")

if (str(data[0]) !=today.strftime("%d.%m.%Y")):
    print('s')
    #tutaj caly update idk jeszcze jak to zrobimy
