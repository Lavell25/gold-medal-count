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

unitedStates = Country(
    country_name='United States',
    gold_medal_count=1180,
    silver_medal_count=959,
    bronze_medal_count=841,
    total_medal_count=2656).save()
unitedKingdom = Country(
    country_name='United Kingdom',
    gold_medal_count=296,
    silver_medal_count=320,
    bronze_medal_count=332,
    total_medal_count=948).save()
germany = Country(
    country_name='Germany',
    gold_medal_count=293,
    silver_medal_count=293,
    bronze_medal_count=306,
    total_medal_count=892).save()
france = Country(
    country_name='France',
    gold_medal_count=258,
    silver_medal_count=289,
    bronze_medal_count=327,
    total_medal_count=874).save()
italy = Country(
    country_name='Italy',
    gold_medal_count=257,
    silver_medal_count=224,
    bronze_medal_count=261,
    total_medal_count=742).save()
china = Country(
    country_name='China',
    gold_medal_count=275,
    silver_medal_count=227,
    bronze_medal_count=194,
    total_medal_count=696).save()
