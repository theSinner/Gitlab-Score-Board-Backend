from datetime import timedelta
from time import time
from threading import Lock

from openid_connect import connect

server_cache = None
server_cache_lock = Lock()
server_cache_expires = None


def get_server(url, client_id, client_secret, protocol=None):
    global server_cache, server_cache_expires, server_cache_lock
    with server_cache_lock:
        now = time()
        if not server_cache_expires or server_cache_expires <= now:
            server_cache = connect(url, client_id, client_secret, protocol)
            server_cache_expires = now + timedelta(hours=1).total_seconds()
        print(server_cache)
        return server_cache
