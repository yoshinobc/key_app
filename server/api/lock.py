import falcon
from ..tools import button

class lock(object):

    def on_post(self,req,resp):
        import RPi.GPIO as GPIO

        resp.status = falcon.HTTP_400

        button.lock()

        resp.status = falcon.HTTP_200

        resp.body = '{"message":locked}'

        return resp
