import requests
from BurgerPlaceFinder import getPlaces
from Geocoding import get_geo

host = "http://api.dajburgera.lucek.com.pl/"
put_url = "http://api.dajburgera.lucek.com.pl/app_dev.php/put-burger"

def burgerPlaceToJSON(bp):
	return {
		'lon': bp.lng, 
		'lat': bp.lat,
		'name': unicode(bp.name, "utf-8"),
		'city': unicode(bp.city, "utf-8"),
		'street': unicode(bp.street, "utf-8"),
		'postalCode': unicode(bp.code, "utf-8"),
		'buildingNumber': bp.bdgNumber,
		'country': unicode(bp.country, "utf-8")
	}

if __name__ == "__main__":
	ffile = open("town_list.txt", "r")
	
	for town in ffile:
		places = getPlaces(town.strip(), 300)
		for p in places:
			l, d = get_geo(p.bdgNumber, p.street, p.city, p.country)
			p.lat, p.lng = l, d
			r = requests.put(put_url, burgerPlaceToJSON(p))
			print burgerPlaceToJSON(p)
			print r