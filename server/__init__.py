import falcon
from server.api.lock import lock
from server.api.lock import unlock

def create_app():
    api = falcon.API()
    locks = lock()
    api.add_route("/locks",locks)

    unlocks = unlock()
    api.add_route("/unlocks",unlock)

    return api
