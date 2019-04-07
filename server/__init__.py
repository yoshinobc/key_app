import falcon
from server.api.lock import lock
from server.api.unlock import unlock
from server.api.add_key import add_key

def create_app():
    api = falcon.API()
    locks = lock()
    api.add_route("/locks",locks)

    unlocks = unlock()
    api.add_route("/unlocks",unlocks)

    add_keys = add_key()
    api.add_route("/addkeys",add_keys)

    return api
