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


class year(BaseModel):
    year = CharField()
    country_name = CharField()
    gold_medal_count = IntegerField()
    silver_medal_count = IntegerField()
    bronze_medal_count = IntegerField()
    total_medal_count = IntegerField()


class Year(BaseModel):
    country_name = CharField()
    year = IntegerField()
    gold_metal_count = IntegerField()
    silver_metal_count = IntegerField()
    bronze_metal_count = IntegerField()
    total_metal_count = IntegerField()


db.connect()
db.drop_tables([Country, Year])
db.create_tables([Country, Year])

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
estonia = Country(
    country_name='Estonia',
    gold_medal_count=14,
    silver_medal_count=11,
    bronze_medal_count=18,
    total_medal_count=43).save()
georgia = Country(
    country_name='Georgia',
    gold_medal_count=10,
    silver_medal_count=12,
    bronze_medal_count=18,
    total_medal_count=40).save()
slovakia = Country(
    country_name='Slovakia',
    gold_medal_count=13,
    silver_medal_count=18,
    bronze_medal_count=9,
    total_medal_count=40).save()
egypt = Country(
    country_name='Egypt',
    gold_medal_count=8,
    silver_medal_count=11,
    bronze_medal_count=19,
    total_medal_count=38).save()
uzbekistan = Country(
    country_name='Uzbekistan',
    gold_medal_count=11,
    silver_medal_count=6,
    bronze_medal_count=20,
    total_medal_count=37).save()
indonesia = Country(
    country_name='Indonesia',
    gold_medal_count=8,
    silver_medal_count=14,
    bronze_medal_count=15,
    total_medal_count=37).save()
ireland = Country(
    country_name='Ireland',
    gold_medal_count=11,
    silver_medal_count=10,
    bronze_medal_count=14,
    total_medal_count=35).save()
thailand = Country(
    country_name='Thailand',
    gold_medal_count=10,
    silver_medal_count=8,
    bronze_medal_count=17,
    total_medal_count=35).save()
india = Country(
    country_name='India',
    gold_medal_count=10,
    silver_medal_count=9,
    bronze_medal_count=16,
    total_medal_count=35).save()
columbia = Country(
    country_name='Columbia',
    gold_medal_count=5,
    silver_medal_count=13,
    bronze_medal_count=16,
    total_medal_count=34).save()
latvia = Country(
    country_name='Latvia',
    gold_medal_count=5,
    silver_medal_count=14,
    bronze_medal_count=11,
    total_medal_count=30).save()
mongolia = Country(
    country_name='Mongolia',
    gold_medal_count=2,
    silver_medal_count=11,
    bronze_medal_count=17,
    total_medal_count=30).save()
portugal = Country(
    country_name='Portugal',
    gold_medal_count=5,
    silver_medal_count=9,
    bronze_medal_count=14,
    total_medal_count=28).save()
nigeria = Country(
    country_name='Nigeria',
    gold_medal_count=3,
    silver_medal_count=11,
    bronze_medal_count=13,
    total_medal_count=27).save()
lithuania = Country(
    country_name='Lithuania',
    gold_medal_count=6,
    silver_medal_count=7,
    bronze_medal_count=13,
    total_medal_count=26).save()
serbia = Country(
    country_name='Serbia',
    gold_medal_count=6,
    silver_medal_count=7,
    bronze_medal_count=11,
    total_medal_count=24).save()
morocco = Country(
    country_name='Morocco',
    gold_medal_count=7,
    silver_medal_count=5,
    bronze_medal_count=12,
    total_medal_count=24).save()
trinidadAndTobago = Country(
    country_name='Trinidad and Tobago',
    gold_medal_count=3,
    silver_medal_count=5,
    bronze_medal_count=11,
    total_medal_count=19).save()
venuzuela = Country(
    country_name='Venzuela',
    gold_medal_count=3,
    silver_medal_count=7,
    bronze_medal_count=9,
    total_medal_count=19).save()
armenia = Country(
    country_name='Armenia',
    gold_medal_count=2,
    silver_medal_count=8,
    bronze_medal_count=8,
    total_medal_count=18).save()
algeria = Country(
    country_name='Algeria',
    gold_medal_count=5,
    silver_medal_count=4,
    bronze_medal_count=8,
    total_medal_count=17).save()
bahamas = Country(
    country_name='Bahamas',
    gold_medal_count=8,
    silver_medal_count=2,
    bronze_medal_count=6,
    total_medal_count=16).save()
tunisia = Country(
    country_name='Tunisia',
    gold_medal_count=5,
    silver_medal_count=3,
    bronze_medal_count=7,
    total_medal_count=15).save()
philippines = Country(
    country_name='Philippines',
    gold_medal_count=1,
    silver_medal_count=5,
    bronze_medal_count=8,
    total_medal_count=14).save()
israel = Country(
    country_name='Israel',
    gold_medal_count=3,
    silver_medal_count=1,
    bronze_medal_count=9,
    total_medal_count=13).save()
chile = Country(
    country_name='Chile',
    gold_medal_count=2,
    silver_medal_count=7,
    bronze_medal_count=4,
    total_medal_count=13).save()
malaysia = Country(
    country_name='Malaysia',
    gold_medal_count=0,
    silver_medal_count=8,
    bronze_medal_count=5,
    total_medal_count=13).save()
dominicanRepublic = Country(
    country_name='Dominican Republic',
    gold_medal_count=0,
    silver_medal_count=8,
    bronze_medal_count=5,
    total_medal_count=13).save()
uganda = Country(
    country_name='Uganda',
    gold_medal_count=4,
    silver_medal_count=4,
    bronze_medal_count=3,
    total_medal_count=11).save()
liechtenstein = Country(
    country_name='Liechtenstein',
    gold_medal_count=2,
    silver_medal_count=2,
    bronze_medal_count=6,
    total_medal_count=10).save()
puertoRico = Country(
    country_name='Puerto Rico',
    gold_medal_count=2,
    silver_medal_count=2,
    bronze_medal_count=6,
    total_medal_count=10).save()
uruguay = Country(
    country_name='Uruguay',
    gold_medal_count=2,
    silver_medal_count=2,
    bronze_medal_count=6,
    total_medal_count=10).save()
pakistan = Country(
    country_name='Pakistan',
    gold_medal_count=3,
    silver_medal_count=3,
    bronze_medal_count=4,
    total_medal_count=10).save()
hongKong = Country(
    country_name='Hong Kong',
    gold_medal_count=2,
    silver_medal_count=3,
    bronze_medal_count=4,
    total_medal_count=9).save()
qatar = Country(
    country_name='Qatar',
    gold_medal_count=2,
    silver_medal_count=1,
    bronze_medal_count=5,
    total_medal_count=8).save()
zimbabwe = Country(
    country_name='Zimbabwe',
    gold_medal_count=3,
    silver_medal_count=4,
    bronze_medal_count=1,
    total_medal_count=8).save()
kyrgystan = Country(
    country_name='Kyrgystan',
    gold_medal_count=0,
    silver_medal_count=3,
    bronze_medal_count=4,
    total_medal_count=7).save()
moldova = Country(
    country_name='Moldova',
    gold_medal_count=0,
    silver_medal_count=2,
    bronze_medal_count=4,
    total_medal_count=6).save()

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

    if request.method == 'POST':
        country = request.get_json()
        country = dict_to_model(Country, country)
        country.save()
        country = model_to_dict(country)
        country = jsonify(country)
        return country

    if request.method == 'PUT':
        updated_country = request.get_json()
        country = Country.get(Country.id == id)
        country.country_name = updated_country['country name']
        country.gold_medal_count = updated_country['gold metal count']
        country.silver_medal_count = updated_country['silver metal count']
        country.bronze_medal_count = updated_country['bronze metal count']
        country.total_medal_count = updated_country['total metal count']

    if request.method == 'DELETE':
        country = Country.get(Country.id == id)
        country.delete_instance()
        return jsonify({"deleted": True})


app.run(port=9000, debug=True)
