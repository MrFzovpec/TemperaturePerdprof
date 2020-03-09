from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
import json
import requests


def get_areas_list(request):
    city_id = request.GET['city_id']
    url = f'http://dt.miet.ru/ppo_it/api/{city_id}'
    response = requests.get(
        url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']['area_count']
    return HttpResponse(json.dumps({'areas_count': response}))


def get_houses_list(request):
    city_id = request.GET['city_id']
    area_id = request.GET['area_id']
    url = f'http://dt.miet.ru/ppo_it/api/{city_id}/{area_id}'
    response = requests.get(
        url, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']
    return HttpResponse(json.dumps(response))


def get_apartment_list(request):
    city_id = request.GET['city_id']
    area_id = request.GET['area_id']
    house_id = request.GET['house_id']

    url = f'http://dt.miet.ru/ppo_it/api/{city_id}/{area_id}/{house_id}'
    response = requests.get(url, headers={
                            'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']['apartment_count']

    return HttpResponse(json.dumps(response))
