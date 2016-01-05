import cherrypy
import cgi
import os.path
import hashlib
import random
from time import time
from configReader import ConfigReader

configReader = ConfigReader(name = "serverConfig.txt")
keys = configReader.getKeys()
location = keys['location']
adjectivesFile = open("adjectives.txt", "r")
adjectives = [line.rstrip() for line in adjectivesFile]
adjectivesFile.close()

class Main():
	@cherrypy.expose
	def index(self):
		raise cherrypy.HTTPError(403)

	@cherrypy.expose
	def upload(self, *args, **kwargs):
			timeBytes = bytes(str(time()), "utf-8")
			timeHash = hashlib.md5(timeBytes).hexdigest()[0:6]
			adjective = random.choice(adjectives)
			name = adjective + timeHash + ".png"
			cherrypy.request.body.process()
			parts = cherrypy.request.params['file']
			outFile = open(os.path.join(location, name), 'wb')
			if parts != None:
				for part in parts:
					outFile.write(part.fullvalue())
				outFile.close()
				return name
			else:
				raise ValueError

application = cherrypy.tree.mount(Main(), '/')
if __name__=='__main__':
	cherrypy.server.socket_host='0.0.0.0'
	cherrypy.engine.start()
	cherrypy.engine.block()
