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
    res = root.reboot()
    print(template.load(u"reboot.html", {}))
  except Exception as e:
    print(u"folder_sizes.py exeption: I/O error: {0}".format( str(e)))
