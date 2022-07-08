import pymongo
import starships as ships
import pprint
import starships

client = pymongo.MongoClient()

db = client['starwars']

starships.insert_into_collection()