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



debug = '-v' in sys.argv
baseUrl = "http://track.intracworks.com"
user = { 'email' : 'admin', 'password' : 'jaihanuman4US$' }


def login():
    request = urllib2.Request(baseUrl + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    if debug:
        print ('\nlogin: %s\n' % repr(json.load(response)))
    return response.headers.get('Set-Cookie')

def get_device(cookie):
    request = urllib2.Request(baseUrl + '/api/users')
    request.add_header('Cookie', cookie)
    response = urllib2.urlopen(request)
    data = json.load(response)
    sizex = len(data)
    print data


def add_device(cookie, password):
    request = urllib2.Request(baseUrl + 'api/users/{9}')
    request.add_header('Cookie', cookie)
    #request.add_header('Content-Type', 'application/json')
    device = { 'deviceLimit': -1,'disabled': False,'id': 9,'coordinateFormat': u'','readonly': True,'userLimit': -1,'latitude': 0.0,'expirationTime': None,'email': u'praveen.namburi@gmail.com','map': u'', u'administrator': False,'phone': u'','password': password, 'limitCommands': False, 'deviceReadonly': False, 'name': 'Praveen', 'poiLayer': u'', 'zoom': 0, 'longitude': 0.0, 'token': None, 'attributes': {}, 'login': u'','twelveHourFormat': False }
    request.get_method = lambda: 'PUT' 
    response = urllib2.urlopen(request, json.dumps(device))
    data = json.load(response)

    response.close()
    return data


cookie = login()
#get_device(cookie)
add_device(cookie, "testpass")

