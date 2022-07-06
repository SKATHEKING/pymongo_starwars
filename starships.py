import requests
import pprint

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
	while response.status_code != 404 and response.status_code == 200:
		try:
			requests.get(response.json()['next'])
			response = requests.get(response.json()['next'])
			pprint.pprint(response.text)
		except:
			break

#gets pilots from one single page
def get_pilots_from_single_page():
	response = requests.get('https://swapi.dev/api/starships/?page=1')
	pilots = response.json()['results'][4]['pilots']

	for pilot in pilots:
		do_call(pilot)
		pprint.pprint(do_call(pilot))


#call all pilots apis from within the json api
def all_pilot_api_call():
	api_call_all()
	pilots = response.json()['results'][0]['pilots']

	for pilot in pilots:
		do_call(pilot)
		pprint.pprint(do_call(pilot).json())



#api_call_check()
#api_call_all()
get_pilots_from_single_page()
#all_pilot_api_call()