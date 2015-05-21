import redis

# Globals
global redis_obj
global hashname

global readerkeyform
global writerkeyform

global maxcache

# Check for Redis availability
# Return False for non-connectivity and True otherwise
def RedisAvailable():
    global redis_obj
    if redis_obj is None:
        print 'Redis DB not connected.'
        return False
    return True

# Initialize
# initialize RedisDB connection
# Return error=False for success and error=True for failure
def Init(host, port):
    global hashname, redis_obj, maxcache, readerkeyform, writerkeyform
    hashname = 'pyapp:httpserobj'
    readerkeyform = 'pyapp:reader'
    writerkeyform = 'pyapp:writer'
    maxcache = 10000
    redis_obj = redis.StrictRedis(host=host, port=port, db=0)
    if redis_obj is None:
        print 'Connection with Redis DB cannot be established.'
        return True
    return False

# Store new URL
# adds a http_id specific key and httpserobj value
# Return error=False for success and error=True for failure
def Store(http_id, httpserobj):
    global hashname
    if RedisAvailable():
        redis_obj.hset(hashname, http_id, httpserobj)
        return False
    return True

# Store new URL
# adds a http_id specific key and httpserobj value
# Return error=False for success and error=True for failure
def Purge(http_id):
    global hashname
    if RedisAvailable():
        redis_obj.hdel(hashname, http_id)
        return False
    return True

# Fetch URL
# fetch httpserobj for a http_id specific key
# Return httpserobj for success and None for failure
def Fetch(http_id):
    global hashname
    if RedisAvailable():
        return redis_obj.hget(hashname, http_id)

# Store reader's latest action
# adds a http_id specific key and httpserobj value
# Return error=False for success and error=True for failure
def StoreActionReader(http_id):
    global readerkeyform
    if RedisAvailable():
        redis_obj.set(readerkeyform, http_id)
        return False
    return True

# Fetch reader's latest action
# fetch httpserobj for a http_id specific key
# Return httpserobj for success and None for failure
def FetchActionReader():
    global readerkeyform
    if RedisAvailable():
        return redis_obj.get(readerkeyform)

# Store bare minimum key and value for writer
# adds a http_id specific key and httpserobj value
# Return error=False for success and error=True for failure
def StoreActionWriter(http_id):
    global writerkeyform
    if RedisAvailable():
        redis_obj.set(writerkeyform, http_id)
        return False
    return True

# Fetch writer's latest action
# fetch httpserobj for a http_id specific key
# Return httpserobj for success and None for failure
def FetchActionWriter():
    global writerkeyform
    if RedisAvailable():
        return redis_obj.get(writerkeyform)
