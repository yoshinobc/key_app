import falcon
from server.api.lock import lock
from server.api.lock import unlock
from server.api.add_key import add_key

def create_app():
    api = falcon.API()
    locks = lock()
    api.add_route("/locks",locks)

    unlocks = unlock()
    api.add_route("/unlocks",unlock)

    add_key = add_key()
    api.add_route("/addkey",add_key)

    return api
