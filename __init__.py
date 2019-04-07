import falcon
from server.api.lock import lock
from server.api.lock import unlock

def create_app():
    api = falcon.API()
    lock = lock()
    api.add_route("/locks",lock)

    unlock = unlock()
    api.add_route("/unlocks",unlock)

    return api
