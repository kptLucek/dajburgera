
import sys
import re
import urllib2

#fileName = sys.argv[1]

kStartAddressTag = "<address>"
kEndAddressTag = "</address>"

kYelpBaseURL = "http://www.yelp.com/search?find_desc=burgers&find_loc="

def getYelpPage(city, offset):
  yelpURL = kYelpBaseURL + city + "&start=" + str(offset)
  request = urllib2.urlopen(yelpURL)
  return request.read()

class BurgerPlace:
  def __init__(self, addr):
    splitted = addr.split(",")
    self.addr = addr
    self.street = splitted[0].rsplit(' ', 1)[0]
    self.bdgNumber = splitted[0].rsplit(None, 1)[-1]
    self.code = splitted[1].strip().split(' ')[0]
    self.city = splitted[1].strip().split(' ')[1]
    self.country = splitted[2].strip()
  def __str__(self):
    return self.addr;
 
def toBurgerPlaces(addresses):
  result = []
  for addr in addresses:
    try:
      result.append(BurgerPlace(addr))
    except:
      print("skipped: " + addr)
    
  return result
  
  
def getAddresses(city, number):
  addresses = []

  readAddress = False
  currentAddress = ""

  f = getYelpPage(city, 10)

  for line in f.split('\n'):
    if kStartAddressTag in line:
      readAddress = True
      continue

    if kEndAddressTag in line:
      addresses.append(currentAddress)
      currentAddress = ""
      readAddress = False
      continue

    if readAddress:
      currentAddress += line.strip()
      continue

  return addresses

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
  print("\n".join(places))
    

def getPlaces(city, number):
  addresses = getAddresses("warsaw", 10)
  addresses = cleanAddresses(addresses)
  burgerPlaces = toBurgerPlaces(addresses)
  #printBurgerPlaces(addresses)
  return burgerPlaces
  

