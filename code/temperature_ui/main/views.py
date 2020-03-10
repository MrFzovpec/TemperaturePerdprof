from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
import json
import requests

# first task
def index(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    collection_cities = db['cities']
    cities = [city for city in collection_cities.find()]
    return render(request, 'tasks/first.html', {'cities': cities})


def first(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    collection_cities = db['cities']
    cities = [city for city in collection_cities.find()]

    city_id = request.GET['city']
    city_name = collection_cities.find_one(
        {'city_id': int(city_id)})['city_name']
    area_id = request.GET['area']
    house_id = request.GET['house']
    apartment_id = request.GET['apartment']

    url = f'http://dt.miet.ru/ppo_it/api/{city_id}/{area_id}/{house_id}/{apartment_id}'

    temperature = requests.get(
        url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']['temperature']
    return render(request, 'tasks/first.html', {'cities': cities,
                                                'temperature': temperature,
                                                'city_name': city_name,
                                                'area_id': area_id,
                                                'house_id': house_id,
                                                'apartment_id': apartment_id})

#second task

def second_task(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    temperature_cities = db.cities_temperature
    data = list(temperature_cities.find({'city_id': 1}))
    temperature = [['День', 'Температура на улице']]
    for temp in data:
        temperature.append([temp['counter'] + 1, temp['temperature']])

    return render(request, 'tasks/second.html', {'temperature': temperature})

def third_task(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    collection_cities = db.cities
    cities = list(collection_cities.find())
    apart_temp = db.apartment_temp
    temps = list(apart_temp.find({'area_id': 1, 'house_id': 1, 'apartment_id': 1}))
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
    return render(request, 'tasks/third.html', {'temperature': temperature})

def forth_task(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    collection_cities = db.apartment_temp
