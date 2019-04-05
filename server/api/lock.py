import falcon
from ..tools import button
from ..tools import check_user

class lock(object):

    def on_post(self,req,resp):
        import RPi.GPIO as GPIO

        resp.status = falcon.HTTP_400
        body = req.stream.read()
        data = json.loads(body)
        flag = data["key_flag"]
        if flag:
            body = req.get_header("Authorization")
            data = json.loads(body)
            token = data["token"]
            name = data["name"]
            if not check_user(name,token):
                resp.status = falcon.HTTP_400
                resp.body = '{"message":fails locked}'
                return resp

        button.lock()

        resp.status = falcon.HTTP_200

        resp.body = '{"message":successful locked}'

        return resp
