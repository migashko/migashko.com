#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

import os, sys
import template
from urllib.parse import urlparse
from urllib.parse import parse_qs
import root

if __name__ == '__main__':
  try:
    g={}
    g["result"]="Непонятно"
    uri = os.environ['REQUEST_URI']
    query = urlparse(uri).query
    par = parse_qs(query)
    if 'cmd' in par:
      service=par['name'][0]
      cmd=par['cmd'][0] 
      if par['cmd'][0]=="restart":
        res = root.restart(service)
        g["result"]= service + " перезапущен"
      elif par['cmd'][0]=="start":
        res = root.start(service)
        g["result"]= service + " запущен"
      elif par['cmd'][0]=="stop":
        res = root.stop(service)
        g["result"]= service + " остановлен"
      if res:
        g["result"]= "Error: " + service + ": " + res
    
    print(template.load(u"service_ctl.html", g))
  except Exception as e:
    print(u"I/O error: {0}".format( str(e)))
