import requests
import json
from pymongo import MongoClient
import pymongo

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
        self.db = self.client['predprof']
        self.collection_cities = self.db['cities']
        self.collection_cities_temperature = self.db['cities_temperature']
        self.collection_ap_temp = self.db['apartment_temp']

    def add_city(self, city):
        self.collection_cities.insert_one(city)
    def add_city_data(self, city_data):
        self.collection_cities_temperature.insert_one(city_data)
    def add_apartment(self, data):
        self.collection_ap_temp.insert_one(data)
    def drop_cities(self):
        self.collection_cities.drop()
    def drop_cities_data(self):
        self.collection_cities_temperature.drop()
