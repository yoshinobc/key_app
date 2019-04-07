import falcon
from ..tools import add_user


class add_key(object):

    def on_post(self,req,resp):
        import secrets

        body = req.stream.read()
        data = json.loads(body)

        body = req.get_header("Authorization")
        data = json.loads(body)

        name = data['name']
        token = secrets.token_hex()
        code = add_user(name,token)
        if code:
            print("Successful Add User")
            resp.status = falcon.HTTP_200
            resp.body = '{"message":successful add key}'
            resp.set_header(token)
        else:
            print("Fail Add User")
            resp.status = falcon.HTTP_400
            resp.body = '{"message":fail add key}'

        return resp
