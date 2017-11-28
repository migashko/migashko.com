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
    res = root.run_du("/hdd")
    #res = root.run_du("/home/migashko")
    line = res.split('\n')
    for l in line:
      try:
        s,n = l.split('\t')
        g[n]=s
      except:
        pass
    #print(g)
    print(template.load(u"folder_sizes.html", g))
  except Exception as e:
    print(u"folder_sizes.py exeption: I/O error: {0}".format( str(e)))
