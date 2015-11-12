#!/usr/bin/env python3

from configReader import ConfigReader
import sys
import os, os.path
from time import time
from math import floor
import hashlib
import random
import requests

f = open('adjectives.txt', 'r')
adjectives = [line.rstrip() for line in f]
f.close()
configReader = ConfigReader(name = "clientConfig.txt")
path = sys.argv[1]
timeBytes = bytes(str(time()), "utf-8")
timeHash = hashlib.md5(timeBytes).hexdigest()[0:6]
adjective = random.choice(adjectives)
keys=configReader.getKeys()
endpoint = keys['endpoint']
username = keys['username']
password = keys['password']
finalLocation = keys['finalLocation']
urlPath = adjective+timeHash+".png"

print("Uploading %s as %s to %s" % (path,  urlPath,  endpoint))
r = requests.post(endpoint, 
	auth = (username, password), 
	params = {'name':urlPath}, 
	files = {'file':open(path, 'rb')})
print(r.status_code)

if r.status_code == 200:
	print(os.path.join(finalLocation, urlPath))
	os.system("echo '%s'|pbcopy" % os.path.join(finalLocation, urlPath))
else:
	print(r.text)
