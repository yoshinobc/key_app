class AppResource(object):
    def on_post(self,req,resp):

app = application = falcon.API()
lock = lock.Resource()
unlock = unlock.Resourcec()

api.add_route("/lock",lock)
api.add_route("/unlock",unlock)
