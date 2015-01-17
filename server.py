import cherrypy
import cgi
from configReader import ConfigReader
import tempfile

class FileFieldStorage(cgi.FieldStorage):
    def make_file(self,binary=None):
        return tempfile.NamedTemporaryFile(delete=True)
def noBodyProcess():
    cherrypy.request.process_request_body = False
    
class Main():
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPError(403)
    @cherrypy.expose
    def upload(self,**kwargs):
            cherrypy.request.body.process()
            parts = cherrypy.request.params['file']
            outFile = open('/home/ollien-data/screenshots/'+cherrypy.request.params['name'],'w')
            for part in parts:
                outFile.write(part.fullvalue())
            outFile.close()
            print 'written!'
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(Main())
