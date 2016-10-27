#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

import os, sys
#import codecs
#import subprocess
import template
from urllib.parse import urlparse
from urllib.parse import parse_qs
import root

#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

if __name__ == '__main__':
  try:
    g={}
    g["result"]="Непонятно"
    uri = os.environ['REQUEST_URI']
    query = urlparse(uri).query
    par = parse_qs(query)
    if 'cmd' in par:
      if par['cmd'][0]=="restart":
        res = root.restart(par['name'][0])
        g["result"]= par['name'][0] + " перезапущен"
      elif par['cmd'][0]=="start":
        res = root.start(par['name'][0])
        g["result"]= par['name'][0] + " запущен"
      elif par['cmd'][0]=="stop":
        res = root.stop(par['name'][0])
        g["result"]= par['name'][0] + " остановлен"
      if res:
        g["result"]= "Error: " + par['name'][0] + ": " + res
    
    
    
    
    #print('template.load(u"service_ctl.tpl", g)')
    print(template.load(u"service_ctl.tpl", g))
    #
    #for n in os.environ:
    #  print("{0}={1}<br/>".format(n,os.environ[n]))
    #print os.environ['HOME']

  except Exception as e:
    print(u"I/O error: {0}".format( str(e)))
