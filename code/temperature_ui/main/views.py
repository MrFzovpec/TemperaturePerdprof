from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
import json
import requests

def get_areas_list(request):
    city_id = request.GET['city_id']
    url = f'http://dt.miet.ru/ppo_it/api/{city_id}'
    response = requests.get(url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']['area_count']
    return HttpResponse(json.dumps({'areas_count': response}))

def get_houses_list(request):
    city_id = request.GET['city_id']
    area_id = request.GET['area_id']
    url = f'http://dt.miet.ru/ppo_it/api/{city_id}/{area_id}'
    response = requests.get(url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']
    return HttpResponse(json.dumps(response))

def get_apartment_list(request):
    city_id = request.GET['city_id']
    area_id = request.GET['area_id']
    house_id = request.GET['house_id']

    url = f'http://dt.miet.ru/ppo_it/api/{city_id}/{area_id}/{house_id}'
    response = requests.get(url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']['apartment_count']

    return HttpResponse(json.dumps(response))



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
    area_id = request.GET['area']
    house_id = request.GET['house']
    apartment_id = request.GET['apartment']

    url = f'http://dt.miet.ru/ppo_it/api/{city_id}/{area_id}/{house_id}/{apartment_id}'

    temperature = requests.get(url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']['temperature']
    return render(request, 'tasks/first.html', {'cities': cities, 'temperature': temperature})
