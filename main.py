#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import StringIO
import xml.dom.minidom
from xml.dom.minidom import Node
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

opener = urllib2.build_opener()

token  = [];
length = [];
ntype  = [];
script = [];
pos    = [];

def active_auth(key):
    request_url = 'http://asia.search.yahooapis.com/cas/v1/AuthBootUp.php'
    values={'appid':key}
    post_data = urllib.urlencode(values)
    response  = opener.open(request_url, post_data)
    print response.readlines()

def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

def get_analyze_result(data):
    request_url = 'http://asia.search.yahooapis.com/cas/v1/ws';
    appid       = 'aY7N4aLV34HZPGVrI0mBhcy0_TuV6YnuCRof4JGX6VFo0c0HFGcTUfuK147m'

    values = {'appid':appid,
              'content':data}

    post_data = urllib.urlencode(values)
    response  = opener.open(request_url, post_data)

    xml_file  = response.readlines()[1][:-91]
    doc = xml.dom.minidom.parse(StringIO.StringIO(xml_file))

    for nodes in doc.getElementsByTagName('token'):
        token.append(getText(nodes.childNodes).encode('utf8'))
    for nodes in doc.getElementsByTagName('length'):
        length.append(getText(nodes.childNodes).encode('utf8'))
    for nodes in doc.getElementsByTagName('type'):
        ntype.append(getText(nodes.childNodes).encode('utf8'))
    for nodes in doc.getElementsByTagName('script'):
        script.append(getText(nodes.childNodes).encode('utf8'))
    for nodes in doc.getElementsByTagName('pos'):
        pos.append(getText(nodes.childNodes).encode('utf8'))

def test_for_result():
    for i in range(len(token)):
        print "%s %s %s %s %s" % (token[i],length[i],ntype[i],script[i],pos[i])

#active_auth('aY7N4aLV34HZPGVrI0mBhcy0_TuV6YnuCRof4JGX6VFo0c0HFGcTUfuK147m')
data = raw_input("input data:")
get_analyze_result(data)
test_for_result()
