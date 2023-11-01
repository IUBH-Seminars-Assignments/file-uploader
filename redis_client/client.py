import redis
from time import sleep

class RedisClient:

    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db
        self.client = redis.Redis(host=host, port=port, db=db)

    def get(self, key):
        return self.client.get(key)
    
    def get_with_block(self, key):
        while self.client.get(key) == None:
            sleep(1)
        return self.client.get(key)
    
    def set(self, key, value):
        val = self.client.set(key, value)
        self.client.expire(key, 300)
        return val
    
rc = RedisClient(host='redis', port=6379, db=0)
    