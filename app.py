#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get

@route('/')
def hello():
  return '<h1>Hello World!</h1>'
  
run(host='0.0.0.0', port=argv[1])
