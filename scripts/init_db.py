#!/usr/bin/python

"""
create pizzaservice db and pizzas and extras collections from valid json
"""
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.pizzaservice

with open('../data/json/pizzas.json') as data:
    data = json.load(data)
    db.pizzas.drop()
    db.pizzas.insert_many(data["Pizza"])
    db.extras.drop()
    db.extras.insert_many(data["Extras"])
    db.orders.drop()
