#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import sys
import json
import urllib
from bottle import *
from sys import *
from urllib import *

with urllib.request.urlopen("http://apis.is/concerts") as url:
    data = json.loads(url.read().decode())

		
@route('/')
def index():
     return template('index', data=data)
  
run(host='0.0.0.0', port=argv[1])
