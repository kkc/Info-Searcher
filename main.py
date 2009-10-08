#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

opener = urllib2.build_opener()

def active_auth(key):
    request_url = 'http://asia.search.yahooapis.com/cas/v1/AuthBootUp.php'
    values={'appid':key}
    post_data = urllib.urlencode(values)
    response  = opener.open(request_url, post_data)
    print response.readlines()

def get_analyze_result(data):
    request_url = 'http://asia.search.yahooapis.com/cas/v1/ws';
    appid       = 'aY7N4aLV34HZPGVrI0mBhcy0_TuV6YnuCRof4JGX6VFo0c0HFGcTUfuK147m'

    values = {'appid':appid,
              'content':data}
    post_data = urllib.urlencode(values)
    response = opener.open(request_url, post_data)
    for line in response.readlines():
        print line

#active_auth('aY7N4aLV34HZPGVrI0mBhcy0_TuV6YnuCRof4JGX6VFo0c0HFGcTUfuK147m')
data = raw_input("input data:")
get_analyze_result(data)
