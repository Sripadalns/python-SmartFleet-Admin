# -*- coding: utf-8 -*-
"""
Created on Thu May 03 14:02:23 2018

@author: sripals
"""
import sys
import urllib
import urllib2
import json
import datetime
from dateutil import parser
import dateparser
from datetime import date


debug = '-v' in sys.argv
baseUrl = "http://track.intracworks.com"
user = { 'email' : 'admin@intracworks.com', 'password' : 'jaihanuman4US$' }
bus_list =[]

def login():
    request = urllib2.Request(baseUrl + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    if debug:
        print ('\nlogin: %s\n' % repr(json.load(response)))
    return response.headers.get('Set-Cookie')

def get_device(cookie):
    request = urllib2.Request(baseUrl + '/api/devices')
    request.add_header('Cookie', cookie)
    response = urllib2.urlopen(request)
    data = json.load(response)
    sizex = len(data)
    print data
    today = (datetime.datetime.today()).replace(microsecond = 0)
    for loop in range( 0,sizex):
        x=data[loop]
        time_device=dateparser.parse( x['lastUpdate'],date_formats=['%Y-%m-%d'])
        time_updated= datetime.datetime.strftime((time_device),"%Y-%m-%d %H:%M:%S")
        time_updated = datetime.datetime.strptime(time_updated,"%Y-%m-%d %H:%M:%S")
        print (today - time_updated).total_seconds()
        if (((today - time_updated).total_seconds())) > 864 :
           bus_list.append(x['name'])
        else:
           print "Good"
    

        print x['status']

cookie = login()
get_device(cookie)
print bus_list
