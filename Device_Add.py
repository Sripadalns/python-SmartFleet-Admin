# -*- coding: utf-8 -*-
"""
Created on Thu May 03 14:02:23 2018

@author: sripals
"""
import sys
import urllib
import urllib2
import json

debug = '-v' in sys.argv
baseUrl = "http://track.intracworks.com"
user = { 'email' : 'admin', 'password' : 'jaihanuman4US$' }

def login():
    request = urllib2.Request(baseUrl + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    if debug:
        print ('\nlogin: %s\n' % repr(json.load(response)))
    cookie = response.headers.get('Set-Cookie')
    response.close()
    return cookie

def add_device(cookie, name,unique_id):
    request = urllib2.Request(baseUrl + '/api/devices')
    request.add_header('Cookie', cookie)
    request.add_header('Content-Type', 'application/json')
    device = { 'name' : name, 'uniqueId' : unique_id,'category' : 'Bus' }
    response = urllib2.urlopen(request, json.dumps(device))
    data = json.load(response)
    response.close()
    return data['id']

cookie = login()
add_device(cookie,382505)
