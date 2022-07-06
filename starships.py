import requests
import pprint

#does singular api call
response = requests.get('https://swapi.dev/api/starships/?page=1')

#prints status code for api call as well as results
def api_call_check():
	print(response)
	pprint.pprint(response.text)

#loops through all pages and does api call whilst printing their values
def api_call_all():
	response = requests.get('https://swapi.dev/api/starships/?page=1')
	while response.status_code != 404 and response.status_code == 200:
		try:
			requests.get(response.json()['next'])
			response = requests.get(response.json()['next'])
			pprint.pprint(response.text)
		except:
			break

api_call_check()
api_call_all()