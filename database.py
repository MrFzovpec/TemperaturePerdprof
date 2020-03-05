import requests
import json
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://Petr:GPpetr1309@cluster0-kil4l.mongodb.net/test?retryWrites=true&w=majority')
        self.db = self.client['predprof']
        self.collection = self.db['temperature']

    def add(self, city_data):

        if self.collection.find_one({'day': city_data['day']}) == None:
            self.collection.insert_one(city_data)

    def load(self, city_id):
        pass
