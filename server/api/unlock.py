import falcon
import json
from ..tools import button
from ..tools import check_user

class unlock(object):

    def on_get(self,req,resp):
        import RPi.GPIO as GPIO

        #flag = data["key_flag"]
        flag = False
        if flag:
            body = req.get_header("Authorization")
            data = json.loads(body)
            token = data["token"]
            name = data["name"]
            if not check_user(name,token):
                resp.status = falcon.HTTP_400
                resp.body = '{"message":fails unlocked}'
                return resp

        button.unlock()
        print("unlock")
        resp.status = falcon.HTTP_200

        resp.body = '{"message":unlocked}'

        return resp
