#!/usr/bin/env python3

from configReader import ConfigReader
import sys
import os, os.path
from time import time
from math import floor
import hashlib
import random
import requests

configReader = ConfigReader(name = "clientConfig.txt")
path = sys.argv[1]
keys = configReader.getKeys()
endpoint = keys['endpoint']
username = keys['username']
password = keys['password']
finalLocation = keys['finalLocation']

print("Uploading to %s" % (endpoint))
r = requests.post(endpoint, 
	auth = (username, password), 
	files = {'file': open(path, 'rb')})

print(r.status_code)

if r.status_code == 200:
	urlPath = os.path.join(finalLocation, r.text)
	print(urlPath)
	os.system("echo '%s'|pbcopy" % urlPath)
else:
	print(r.text)
