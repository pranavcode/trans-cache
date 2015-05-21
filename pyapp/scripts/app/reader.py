import httpbase
import pickle
import sys
import string
import time
import random
import requests

global http_id

def ReadCacheObject():
    global http_id
    data = httpbase.Fetch(http_id)
    if data != None:
        http_obj = pickle.loads(data)
        timestamp = int(time.time())
        logstr = str(timestamp)+' '+str(http_id)+' '+str(http_obj.url)
        with open("/data/reader.log", "a") as myfile:
                myfile.write(logstr+'\n')
        print logstr
        error = httpbase.Purge(http_id)
        if error:
            print 'Error: Unable to purge objects from cache.\n'
        else:
            http_id = http_id + 1
            if http_id > httpbase.maxcache:
                http_id = 0

if __name__ == "__main__":
    global http_id
    http_id = 0
    error = httpbase.Init('192.168.59.103','6379')
    if error == False:
        while 1:
            ReadCacheObject()
