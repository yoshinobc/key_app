import falcon
from key_app.api.lock import lock

def create_app():
    api = falcon.API()
    locks = lock()
    api.add_route("/locks",locks)

    unlocks = unlock()
    api.add_route("/unlocks",unlock)

    return api
