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

# second task


def second_task(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    results = db.results
    data = results.find_one({'num_task': 0})['value']

    return render(request, 'tasks/second.html', {'temperature': data})


def third_task(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    results = db.results
    data = results.find_one({'num_task': 1})['value']

    return render(request, 'tasks/third.html', {'temperature': data})


def forth_task(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    results = db.results
    data = results.find_one({'num_task': 2})['value']

    return render(request, 'tasks/forth.html', {'temperature': data})

def avarage(request):
    client = MongoClient(
        'mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
    db = client['predprof']
    results = db.results
    data = results.find_one({'num_task': 3})['value']
    return render(request, 'tasks/avarage.html', {"temperature": data})
