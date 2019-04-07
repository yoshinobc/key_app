import falcon
import json

class HogeResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({ 
                      "result": True, 
                      "message": "success!",
                    })

api = falcon.API()
hoge = HogeResource()

api.add_route('/test',hoge)

from wsgiref import simple_server
httpd = simple_server.make_server("localhost",8000,api)
httpd.serve_forever()
