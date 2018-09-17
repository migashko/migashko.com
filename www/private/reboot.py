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
    res={}
    res["text"] = root.reboot()
    print(template.load(u"reboot.html", res))
  except Exception as e:
    print(u"reboot.py exeption: I/O error: {0}".format( str(e)))
