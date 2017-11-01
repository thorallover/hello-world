

import bottle
import sys
import json
import urllib.request
from bottle import *
from sys import *

with urllib.request.urlopen("http://apis.is/concerts") as url:
    data = json.loads(url.read().decode())

		
@route('/ind')
def index():
     return template('index', data=data)
  
run(host='0.0.0.0', port=argv[1])
