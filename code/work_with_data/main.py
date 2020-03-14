import requests
import json
from pymongo import MongoClient
from datetime import datetime
from database import Database
import time
db = Database()

URL = 'http://dt.miet.ru/ppo_it/api'

# set functions


def add_cities(cities):
    for city in cities:
        db.add_city(city)

def get_cities():
    response = json.loads(requests.get(
        URL, headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).content)['data']
    return response


def get_data(counter, cities):
    for city in cities:
        city_id = city['city_id']
        res = requests.get(
            f'{URL}/{city_id}',
            headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}
        )
        if res.status_code == 200:
            content = res.json()['data']
        for area_id in range(1, 6):
            res_areas = requests.get(
                f'{URL}/{city_id}/{area_id}',
                headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}
            )
            if res_areas.status_code == 200:
                content_areas = res_areas.json()['data']
            for house_id in range(1, 3):
                res_houses = requests.get(
                    f'{URL}/{city_id}/{area_id}/{house_id}',
                    headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}
                )
                if res_houses.status_code == 200:
                    content_houses = res_houses.json()['data']
                for apartment_id in range(1, 3):
                    res_appartment = requests.get(
                        f'{URL}/{city_id}/{area_id}/{house_id}/{apartment_id}',
                        headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}
                    )
                    if res_appartment.status_code == 200:
                        content_appartment = res_appartment.json()['data']
                    else:
                        continue

                    target = {
                        'city_id': city_id,
                        'city_temperature': requests.get(f'{URL}/{city_id}/temperature', headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data'],
                        'area_id': area_id,
                        'apartment_id': apartment_id,
                        'house_id': house_id,
                        'apartment_temperature': content_appartment['temperature'],
                        'counter': counter
                    }
                    db.add_apartment(target)


def add_city_data(cities, counter):
    for i, city in enumerate(cities):
        id = city["city_id"]
        res = requests.get(
            f'{URL}/{id}',
            headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}
        )
        if res.status_code == 200:
            content = res.json()['data']
            content['counter'] = counter
            db.add_city_data(content)


cities = get_cities()
add_cities(cities)

start_ev = int(time.time())
m_range = 24 * 3600
counter = 0

while int(time.time()) - start_ev <= m_range:
    get_data(counter, cities)
    add_city_data(cities, counter)
    counter += 1
    time.sleep(60)
