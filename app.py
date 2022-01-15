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
romania = Country(
    country_name='Romania',
    gold_medal_count=90,
    silver_medal_count=97,
    bronze_medal_count=122,
    total_medal_count=309).save()
cuba = Country(
    country_name='Cuba',
    gold_medal_count=85,
    silver_medal_count=71,
    bronze_medal_count=85,
    total_medal_count=241).save()
bulgaria = Country(
    country_name='Bulgaria',
    gold_medal_count=55,
    silver_medal_count=90,
    bronze_medal_count=85,
    total_medal_count=230).save()
denmark = Country(
    country_name='Denmark',
    gold_medal_count=48,
    silver_medal_count=79,
    bronze_medal_count=79,
    total_medal_count=206).save()
spain = Country(
    country_name='Spain',
    gold_medal_count=49,
    silver_medal_count=72,
    bronze_medal_count=50,
    total_medal_count=171).save()
belgium = Country(
    country_name='Belgium',
    gold_medal_count=44,
    silver_medal_count=56,
    bronze_medal_count=61,
    total_medal_count=161).save()
brazil = Country(
    country_name='Brazil',
    gold_medal_count=37,
    silver_medal_count=42,
    bronze_medal_count=71,
    total_medal_count=150).save()
ukraine = Country(
    country_name='Ukraine',
    gold_medal_count=38,
    silver_medal_count=37,
    bronze_medal_count=72,
    total_medal_count=147).save()
newZealand = Country(
    country_name='New Zealand',
    gold_medal_count=53,
    silver_medal_count=34,
    bronze_medal_count=53,
    total_medal_count=140).save()
greece = Country(
    country_name='Greece',
    gold_medal_count=35,
    silver_medal_count=45,
    bronze_medal_count=41,
    total_medal_count=121).save()
kenya = Country(
    country_name='Kenya',
    gold_medal_count=35,
    silver_medal_count=42,
    bronze_medal_count=36,
    total_medal_count=113).save()
turkey = Country(
    country_name='Turkey',
    gold_medal_count=41,
    silver_medal_count=26,
    bronze_medal_count=37,
    total_medal_count=104).save()
belarus = Country(
    country_name='Belarus',
    gold_medal_count=21,
    silver_medal_count=35,
    bronze_medal_count=47,
    total_medal_count=103).save()
czechRepublic = Country(
    country_name='Czech Republic',
    gold_medal_count=28,
    silver_medal_count=32,
    bronze_medal_count=38,
    total_medal_count=98).save()
southAfrica = Country(
    country_name='South Africa',
    gold_medal_count=27,
    silver_medal_count=33,
    bronze_medal_count=29,
    total_medal_count=89).save()
jamaica = Country(
    country_name='Jamaica',
    gold_medal_count=26,
    silver_medal_count=36,
    bronze_medal_count=25,
    total_medal_count=87).save()
kazakhstan = Country(
    country_name='Kazakhstan',
    gold_medal_count=16,
    silver_medal_count=24,
    bronze_medal_count=40,
    total_medal_count=80).save()
argentina = Country(
    country_name='Argentina',
    gold_medal_count=21,
    silver_medal_count=26,
    bronze_medal_count=30,
    total_medal_count=77).save()
iran = Country(
    country_name='Iran',
    gold_medal_count=24,
    silver_medal_count=23,
    bronze_medal_count=29,
    total_medal_count=76).save()
mexico = Country(
    country_name='Mexico',
    gold_medal_count=13,
    silver_medal_count=24,
    bronze_medal_count=36,
    total_medal_count=73).save()
ethiopia = Country(
    country_name='Ethiopia',
    gold_medal_count=23,
    silver_medal_count=12,
    bronze_medal_count=23,
    total_medal_count=58).save()
northKorea = Country(
    country_name='North Korea',
    gold_medal_count=16,
    silver_medal_count=17,
    bronze_medal_count=23,
    total_medal_count=56).save()
croatia = Country(
    country_name='Croatia',
    gold_medal_count=18,
    silver_medal_count=19,
    bronze_medal_count=15,
    total_medal_count=52).save()
azerbaijan = Country(
    country_name='Azerbaijan',
    gold_medal_count=7,
    silver_medal_count=14,
    bronze_medal_count=28,
    total_medal_count=49).save()
slovenia = Country(
    country_name='Slovenia',
    gold_medal_count=10,
    silver_medal_count=14,
    bronze_medal_count=21,
    total_medal_count=45).save()

app = Flask(__name__)


@app.route('/country', methods=['GET', 'PUT', 'POST', 'DELETE'])
@app.route('/country/<id>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def country(id=None):
    if request.method == 'GET':

        if id:
            country = Country.get(Country.id == id)
            country = model_to_dict(country)
            country = jsonify(country)
            return country

        else:
            countries = []
            for country in Country.select():
                country = model_to_dict(country)
                countries.append(country)
            countries = jsonify(countries)
            return countries

    if request.method == 'Post':
        country = request.get_json()
        country = dict_to_model(Country, country)
        country.save()
        country = model_to_dict(country)
        country = jsonify(country)
        return country
