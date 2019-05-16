#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

import os, sys
import template
import root

if __name__ == '__main__':
  try:
    g={}
    g["text"] = root.reboot()
    print(template.load(u"reboot.html", g))
  except Exception as e:
    print(u"reboot.py exeption: I/O error: {0}".format( str(e)))
