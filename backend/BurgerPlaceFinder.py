
import sys
import re
import urllib2

from BurgerPlace import BurgerPlace

kStartAddressTag = "<address>"
kEndAddressTag = "</address>"
kNameTag = "<span class=\"indexed-biz-name\">"
kOffsetStep = 10

kYelpBaseURL = "http://www.yelp.com/search?find_desc=burgers&find_loc="

def getYelpPage(city, offset):
  yelpURL = kYelpBaseURL + city + "&start=" + str(offset)
  request = urllib2.urlopen(yelpURL)
  return request.read()
 
def toBurgerPlaces(addresses, names):
  result = []
  for addr, name in zip(addresses, names):
    try:
      result.append(BurgerPlace(addr, name))
    except:
      print("skipped: " + name + ", " + addr)
    
  return result
  
def getAddresses(city, number):
  addresses = []
  names = []

  currentAddress = ""
  name = ""

  readAddress = False

  offset = 0

  while (number > 0):
    f = getYelpPage(city, offset)
    
    for line in f.split('\n'):
      if kStartAddressTag in line:
        readAddress = True
        continue

      if kEndAddressTag in line:
        addresses.append(currentAddress)
	names.append(name)
        currentAddress = ""
        readAddress = False
        continue

      if kNameTag in line:
        result = re.match("(.*)<span>(.*)</span>(.*)", line)
        name = result.group(2)
        continue

      if readAddress:
        currentAddress += line.strip()
        continue
    offset += kOffsetStep
    number -= kOffsetStep

  return (addresses, names)

def cleanAddresses(addresses):
  def checkAddress(address):
    if not re.match("(.*),(.*),(.*)", address):
      return False
    return True

  cleaned = [];
  for addr in addresses:
    clean = addr
    clean = clean.replace("<br>", ", ")
    clean = clean.replace("\n", " ")
    if (checkAddress(clean)):
      cleaned.append(clean)
  return cleaned

def printAddresses(addresses):
  print("\n".join(addresses))

def printBurgerPlaces(places):
  for place in places:
    print place
    

def getPlaces(city, number):
  addresses, names = getAddresses(city, number)
  addresses = cleanAddresses(addresses)
  places = toBurgerPlaces(addresses, names)
  #printBurgerPlaces(places)
  return places

getPlaces("warsaw", 40);

