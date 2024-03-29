#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

# sudo apt-get install -y python3-setuptools
# sudo easy_install3 Genshi
import os, sys
import template
from urllib.parse import urlparse
from urllib.parse import parse_qs
import root

if __name__ == '__main__':
  try:
    g={}
    g["result"]="Непонятно"
    g["message"]=""
    g["status"]=""
    uri = os.environ['REQUEST_URI']
    query = urlparse(uri).query
    par = parse_qs(query)
    if 'cmd' in par:
      service=par['name'][0]
      cmd=par['cmd'][0] 
      if par['cmd'][0]=="restart":
        res = root.restart(service)
        g["result"] = service + " перезапущен"
      elif par['cmd'][0]=="start":
        res = root.start(service)
        g["result"]= service + " запущен"
      elif par['cmd'][0]=="stop":
        res = root.stop(service)
        g["result"]= service + " остановлен"
      if res:
        g["result"]= service + " ошибка"
        g["message"]= "Error: " + service + ": " + res
      g["status"] = root.status(service)
      g["name"] = service
    
    print(template.load(u"service_ctl.html", g))
  except Exception as e:
    print(u"service_ctl.py exeption: I/O error: {0}".format( str(e)))
