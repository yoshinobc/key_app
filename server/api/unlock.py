import falcon
import ..tools import button
import ..tools import check_user

class unlock(object):

    def on_post(self,req,resp):
        import RPi.GPIO as GPIO

        resp.status = falcon.HTTP_400
        flag = data["key_flag"]
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

        resp.status = falcon.HTTP_200

        resp.body = '{"message":unlocked}'

        return resp
