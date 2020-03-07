import requests
import json
from pymongo import MongoClient
import pymongo
import time


client = MongoClient('mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
db = client['predprof']
start = time.time()
a = db.apartment_temp.find({ 'city_id': 1, 'area_id': 1, 'house_id': 1}).collation({'locale': "en", 'strength': 1})

finish = time.time()

print(float(finish) - float(start))
