#!/usr/bin/python
import trunofficial
from sys import version_info
#Created by N3V0N <navanchauhan@gmail.com>
#MIT License
py3 = version_info[0] > 2 

if py3:
  print("This Script Requires Python 2")
else:

  response = raw_input("Please enter the number : ")
owner = trunofficial.search(response)
mobile = owner.phone
house = owner.address

print "Owner Name    : ", owner.name
print "Mobile Number : ", mobile.number
print "Country Code  : ", mobile.countrycode
print "City          : ", house.city
print "Area          : ", house.area
print "Mobile Carrier: ", mobile.carrier
print "TimeZone      : ", house.timezone
print "Score         : ", owner.score
print "Spam Score    : ", mobile.spamscore
print "Spam Type     : ", mobile.spamtype
print "Phone Type    : ", mobile.phonetype
print "Owner ID      : ", owner.id
print "Access        : ", owner.access
print "Enhanced      : ", owner.enhanced
print "Internet Addr.: ", owner.internet_address
print "Badges        : ", owner.badges
print "Tags          : ", owner.tags
print "Owner Sources : ", owner.sources
