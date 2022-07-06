import pymongo
import starships as ships
import pprint

client = pymongo.MongoClient()

db = client['starwars']

def printAllShips():
    pprint.pprint(ships.ships['results'])

def loopThroughPage():
    while ships.ships['next'] != None:
        ships.ships['next'].replace()