
import redis

# Redis config
_REDIS_SERVER = 'redis-server'
_REDIS_PORT = 6379
_REDIS_DB = 0
# Data Constants
_HASHES_KEY = "filehashes"
_PATHS_KEY = "paths:"

# Module only initializes if a connection is available
try:
    _CONN = redis.StrictRedis(
            host=_REDIS_SERVER, 
            port=_REDIS_PORT, 
            db=_REDIS_DB)
    _CONN.ping()
except redis.exceptions.ConnectionError as e:
    print("Could not connect to {} on port {}.".format(
        _REDIS_SERVER, _REDIS_PORT))
    print("Redis Error: {}".format(e))
    exit()

#
#   Saves a hash and filepath, increments counter
#
def save_hash(hashstring, filepath):
    # incrementa o score da HASHSTRING em 1.
    # se a hashstring ainda não existe na chave, é criada com score 1.
    # caso contrário, incrementa em 1.
    # funciona como contador para cada HASH.
    _CONN.zincrby(_HASHES_KEY, hashstring, 1)

    # em outra estrutura, associa a HASH com os FILE PATHS
    _CONN.sadd(
            "{}{}".format(_PATHS_KEY, hashstring),
            filepath.encode('utf8', 'surrogateescape')
            )

#
#   Finds all duplicate files (more than ONE of the same hash)
#
def get_duplicate_hashes():
    result = _CONN.zrangebyscore(_HASHES_KEY, 2, "+inf")
    return result

#
#   Returns a list of files for a given hash
#
def get_files(hashstring):
    result = _CONN.smembers("{}{}".format(_PATHS_KEY, hashstring))
    return result


