import requests
import pprint
import pymongo

client = pymongo.MongoClient()

db = client['starwars']

# does singular api call
response = requests.get('https://swapi.dev/api/starships/?page=1')


# does api call
def do_call(url):
    response = requests.get(url).json()
    pprint.pprint(response)
    return response


# prints status code for api call as well as results
def api_call_check():
    print(response)
    pprint.pprint(response.text)


# loops through all pages and does api call whilst printing their values

def api_call_all():
    url = 'https://swapi.dev/api/starships/?page=1'
    response = requests.get(url)
    ships_info = []
    count = 0
    while response.json()['next'] != None:

        for ship in response.json()['results']:
            ships_info.append(ship)

        response = requests.get(response.json()['next'])


    try:
        if response.json()['next'] == None:

            for ship in response.json()['results']:
                ships_info.append(ship)

    except:
        print("ERROR")
    finally:
        for i in ships_info:
            count += 1
        print(count)
        pprint.pprint(ships_info)
        return ships_info


# call all pilots apis from within the json api
def all_pilot_api_call():
    ships = api_call_all()
    list_of_pilots = []

    try:
        for pilots in ships:
            if pilots['pilots'] != [] and pilots['pilots'] != None:
                for pilot in pilots['pilots']:
                    do_call(pilot)
                    list_of_pilots.append(pilot)
                    pprint.pprint(do_call(pilot))
            else:
                print('No pilots were found')

    except:
        print('It was no possible to find any ships')

        return list_of_pilots


# adds starship database to collection
def add_collection():
    db['starships'].insert_many(api_call_all())


# removes collection if it exists
def remove_collection(collection='starships'):
    if db[collection]:
        db[collection].drop()


# inserts into collection all pilots with their corresponding ids
def insert_into_collection():
    for pilot in all_pilot_api_call()['name']:
        pilot_object = db.characters.find({'name:' f'{pilot}'})


# api_call_check()
# print(api_call_all())
# all_pilot_api_call()
# do_call('https://swapi.dev/api/people/39/')
# insert_into_collection()
#add_collection()
# remove_collection()
#api_call_all()
