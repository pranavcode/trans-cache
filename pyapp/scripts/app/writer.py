import datagen
import httpbase
import pickle
import sys
import string
import time
import random
import requests

global http_id

def WriteCacheObject():
    global http_id
    data = httpbase.Fetch(http_id)
    if data == None:
        dummyobj = ""
        if http_id % 2 == 0:
            dummyobj = datagen.GetSerializedRequestObject()
        else:
            dummyobj = datagen.GetSerializedResponseObject()
        httpbase.Store(http_id, dummyobj)
        http_obj = pickle.loads(dummyobj)
        timestamp = int(time.time())
        print str(timestamp)+' '+str(http_id)+' '+str(http_obj.url)
    http_id = http_id + 1
    if http_id > httpbase.maxcache:
        http_id = 0
    

if __name__ == "__main__":
    global http_id
    http_id = 0
    error = httpbase.Init('192.168.59.103','6379')
    if error == False:
        while 1:
            flow = random.randint(0,1000)
            for i in range(0, flow):
                WriteCacheObject()
            time.sleep(5)
