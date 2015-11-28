#!/usr/bin/python

import sys
import re

fileName = sys.argv[1]

kStartAddressTag = "<address>"
kEndAddressTag = "</address>"


def getAddresses():
  addresses = []

  f = open(fileName, 'r')
  readAddress = False
  currentAddress = ""

  for line in f:
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
    
addresses = getAddresses()
addresses = cleanAddresses(addresses)
printAddresses(addresses)

