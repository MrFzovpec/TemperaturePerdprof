import requests
import json
from pymongo import MongoClient
import pymongo
from database import  Database

db = Database()

def average():
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    apart_temp = db.apartment_temp

    data = [['День', 'Средняя температура, ℃']]
    for i in range(230):
        temps = apart_temp.find({'city_id': 2, 'counter': i})
        sums = []
        for temp in temps:
            sums.append(temp['apartment_temperature'])

        data.append([i, sum(sums) / len(sums)])
    dataset = {
        'value': data
    }
    return dataset

def max_temp():
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    apart_temp = db.apartment_temp

    temperatures = [['Район', 'Максимальная температура, ℃']]
    for areaId in range(1, 6):
        temps = list(apart_temp.find({'city_id': 2, 'area_id': areaId}))
        data = sorted(temps, key=lambda t: t['counter'])
        maxes = []
        for temp in data:
            maxes.append(temp['apartment_temperature'])

        temperatures.append([f'{areaId}', max(maxes)])
    dataset = {
        'value': temperatures
    }
    return dataset

def all_cities():
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    collection_cities = db.cities
    cities = list(collection_cities.find())
    apart_temp = db.apartment_temp
    temps = list(apart_temp.find(
        {'area_id': 1, 'house_id': 1, 'apartment_id': 1}))
    iters = int(len(temps))
    while iters % 16 != 0:
        iters -= 1
    headers = [city['city_name'] for city in cities][::-1]
    headers.append('День')
    headers = headers[::-1]
    temperature = [headers]
    for i in range(0, iters, 16):
        data = [temps[i]['counter'] + 1]
        for t in temps[i:i + 16]:
            data.append(t['apartment_temperature'])
        temperature.append(data)
    dataset = {
        'value': temperature
    }
    return dataset

def current_city():
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    temperature_cities = db.cities_temperature
    data = list(temperature_cities.find({'city_id': 1}))
    temperature = [['День', 'Температура на улице']]
    for temp in data:
        temperature.append([temp['counter'] + 1, temp['temperature']])

    dataset = {
        'value': temperature
    }
    return dataset

"""
СОХРАНЕНИЕ ОБРАБОТАННЫХ РЕХУЛЬТАТОВ В MongoDB
"""

# db.result(average(), 3)
# db.result(max_temp(), 2)
# db.result(all_cities(), 1)
# db.result(current_city(), 0)
