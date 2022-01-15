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
sweden = Country(
    country_name='Sweden',
    gold_medal_count=205,
    silver_medal_count=222,
    bronze_medal_count=234,
    total_medal_count=661).save()
australia = Country(
    country_name='Australia',
    gold_medal_count=169,
    silver_medal_count=178,
    bronze_medal_count=215,
    total_medal_count=562).save()
japan = Country(
    country_name='Japan',
    gold_medal_count=183,
    silver_medal_count=172,
    bronze_medal_count=200,
    total_medal_count=555).save()
russia = Country(
    country_name='russia',
    gold_medal_count=196,
    silver_medal_count=164,
    bronze_medal_count=187,
    total_medal_count=547).save()
norway = Country(
    country_name='Norway',
    gold_medal_count=192,
    silver_medal_count=176,
    bronze_medal_count=160,
    total_medal_count=528).save()
canada = Country(
    country_name='Canada',
    gold_medal_count=144,
    silver_medal_count=172,
    bronze_medal_count=209,
    total_medal_count=525).save()
hungary = Country(
    country_name='Hungary',
    gold_medal_count=182,
    silver_medal_count=156,
    bronze_medal_count=180,
    total_medal_count=518).save()
finland = Country(
    country_name='Finland',
    gold_medal_count=144,
    silver_medal_count=148,
    bronze_medal_count=180,
    total_medal_count=472).save()
netherlands = Country(
    country_name='Netherlands',
    gold_medal_count=140,
    silver_medal_count=148,
    bronze_medal_count=163,
    total_medal_count=451).save()
switzerland = Country(
    country_name='Switzerland',
    gold_medal_count=109,
    silver_medal_count=124,
    bronze_medal_count=125,
    total_medal_count=358).save()
southKorea = Country(
    country_name='South Korea',
    gold_medal_count=127,
    silver_medal_count=116,
    bronze_medal_count=114,
    total_medal_count=357).save()
austria = Country(
    country_name='Austria',
    gold_medal_count=83,
    silver_medal_count=115,
    bronze_medal_count=128,
    total_medal_count=326).save()
poland = Country(
    country_name='Poland',
    gold_medal_count=79,
    silver_medal_count=96,
    bronze_medal_count=145,
    total_medal_count=320).save()
