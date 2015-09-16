import cherrypy
import cgi
from configReader import ConfigReader
import os.path
import tempfile

configReader = ConfigReader(name="serverConfig.txt")
keys = configReader.getKeys()
location = keys['location']
class Main():
	@cherrypy.expose
	def index(self):
		raise cherrypy.HTTPError(403)

	@cherrypy.expose
	def upload(self, **kwargs):
			cherrypy.request.body.process()
			parts = cherrypy.request.params['file']
			outFile = open(os.path.join(location, cherrypy.request.params['name']),'w')
			if parts != None:
				for part in parts:
					outFile.write(part.fullvalue())
				outFile.close()
			else:
				raise ValueError

application = cherrypy.tree.mount(Main(), '/')
if __name__=='__main__':
	cherrypy.server.socket_host='0.0.0.0'
	cherrypy.engine.start()
	cherrypy.engine.block()
