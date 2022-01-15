from itertools import count
from wsgiref.util import request_uri
from flask import Flask
from flask import request
from flask import jsonify
from peewee import *

from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('project', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Country(BaseModel):
    country_name = CharField()
    gold_medal_count = IntegerField()
    silver_medal_count = IntegerField()
    bronze_medal_count = IntegerField()
    total_medal_count = IntegerField()


db.connect()
db.drop_tables([Country])
db.create_tables([Country])
