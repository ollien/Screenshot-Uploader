#!/usr/bin/env python

from configReader import ConfigReader
import sys
import os, os.path
import os.path
from time import time
from math import floor
import hashlib
import random
import requests

f = open('adjectives.txt','r')
adjectives = [line.rstrip() for line in f]
f.close()
configReader = ConfigReader(name="clientConfig.txt")
path = sys.argv[1]
timeHash = hashlib.md5(str(time())).hexdigest()[0:6]
adjective = random.choice(adjectives)
keys=configReader.getKeys()
endpoint=keys['endpoint']
username=keys['username']
password=keys['password']
finalLocation=keys['finalLocation']
urlPath = adjective+timeHash+".png"
print "Uploading",path,"as",urlPath,"to",endpoint
r = requests.post(endpoint,auth=(username,password),params={'name':urlPath},files={'file':open(path,'rb')})
print r.status_code
print r.text
if r.status_code==200:
	print os.path.join(finalLocation,urlPath)
	os.system("echo '"+os.path.join(finalLocation,urlPath)+"'|pbcopy")
