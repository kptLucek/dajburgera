import requests
import json
key = 'AIzaSyCPK69oKXCL1VLU7N3gBVHc2bTpfKzKkoo'

def get_geo(nr, street, town='Warsaw', country='Poland'):
	address = nr + "+" + street + ",+" + town + ",+" + country

	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + key)
	js = r.json()
	loc = js['results'][0]['geometry']['location']
	return loc['lat'], loc['lng']