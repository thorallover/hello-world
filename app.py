#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import sys
from bottle import *
from sys import *

@route('/')
def hello():
  return '<h1>Halló Heimur!</h1>'
  
run(host='0.0.0.0', port=argv[1])
