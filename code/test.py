import requests
import json
from pymongo import MongoClient
import pymongo
import time


URL = 'http://dt.miet.ru/ppo_it/api'
city_id = 1
response = requests.get(f'{URL}/{city_id}/1/1/temperature', headers={'X-Auth-Token': 'dn8lq5kcinavtpfn'}).json()['data']
average = 0
