import pymongo
import starships as ships
import pprint

client = pymongo.MongoClient()

db = client['starwars']

