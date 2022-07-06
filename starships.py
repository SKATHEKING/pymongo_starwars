import requests
import pprint
import pymongo

#does singular api call
response = requests.get('https://swapi.dev/api/starships/?page=1')

#does api call
def do_call(url):
	response = requests.get(url)

#prints status code for api call as well as results
def api_call_check():
	print(response)
	pprint.pprint(response.text)


#loops through all pages and does api call whilst printing their values

def api_call_all():
	response = requests.get('https://swapi.dev/api/starships/?page=1')
	ships_info = []
	while response.status_code != 404 and response.status_code == 200:
		try:
			requests.get(response.json()['next'])
			response = requests.get(response.json()['next'])
			pprint.pprint(response.json())
			for ship in response.json()['results']:
				ships_info.append(ship)

			return ships_info
		except:
			break

#call all pilots apis from within the json api
def all_pilot_api_call():

	ships = api_call_all()
	list_of_pilots = []

	try:
		for pilots in ships:
			if pilots['pilots'] != [] :
				for pilot in pilots['pilots']:

					do_call(pilot)
					list_of_pilots.append(pilot)
					pprint.pprint(do_call(pilot))
			else:
				print('No pilots were found')

	except :
		print('It was no possible to find any ships')

	finally:
		return list_of_pilots


#inserts into collection
def insert_into_collection():
	print('to be done ')


#api_call_check()
#print(api_call_all())
all_pilot_api_call()