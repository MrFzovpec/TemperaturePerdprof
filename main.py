import requests
import json
from pymongo import MongoClient
from datetime import datetime
from database import Database
import time
db = Database()
def parse():
    for i in range(16):
        response = requests.get('http://dt.miet.ru/ppo_it/api/{}'.format(i + 1),
                                headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'})
        city_data = json.loads(response.content.decode('utf-8'))['data']
        city_data['day'] = datetime.now()
        for k in range(city_data['area_count']):
            response = json.loads(requests.get('http://dt.miet.ru/ppo_it/api/{}/{}'.format(i + 1, k + 1), headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).content.decode('utf-8'))['data']

            z = 0
            for h in response:
                response[z]['houses'] = []
                house = json.loads(requests.get('http://dt.miet.ru/ppo_it/api/{}/{}/{}/temperature'.format(i + 1, k + 1, h["house_id"]), headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).content.decode('utf-8'))['data']

                response[z]['houses'].append(house)
                z += 1

            city_data['areas_data'] = response
        db.add(city_data)
parse()
