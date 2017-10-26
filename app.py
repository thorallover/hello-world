#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from sys import argv

import bottle
from bottle import *

@route('/')
def hello():
  return '<h1>Hello World!</h1>'
  
run(host='0.0.0.0', port=argv[1])
