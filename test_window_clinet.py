import sys
import urllib
import urllib2
import json
import requests
import datetime
from rand_latlog import rand_latlog
import time

while (1):

    lat,longz = rand_latlog()
    latx = str(lat)
    longx = str(longz)
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timex =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    r = requests.put("http://track.intracworks.com:5055/?id="+(str(382056))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex))
    lat,longz = rand_latlog()
    latx = str(lat)
    longx = str(longz)
    r = requests.put("http://track.intracworks.com:5055/?id="+(str(382057))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex))
    lat,longz = rand_latlog()
    latx = str(lat)
    longx = str(longz)
    r = requests.put("http://track.intracworks.com:5055/?id="+(str(382058))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex))
    
    time.sleep(10)
