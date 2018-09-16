#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8


import os, sys
import codecs
import subprocess

import template
import root


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

if __name__ == '__main__':
  try:
    names=["minidlna", "mpd", "transmission", "mediacenter", "smbd", "lighttpd"]
    dct={}
    dct['services']=[]
    for i in range(len(names)):
      item = {};
      dct['services'].append(item)
      status = root.status(names[i])

      name = names[i]
      item["name"]=names[i]
      item["status"] = status
      if status in ["inactive", "failed"]:
        item["start"] = u"service_ctl.py?name=" + names[i] + "&cmd=start"
      elif status == "active":
        item["restart"] = u"service_ctl.py?name=" + names[i] + "&cmd=restart"
        if names[i]!="lighttpd":
          item["stop"] = u"service_ctl.py?name=" + names[i] + "&cmd=stop"
      elif not status in ["unknown"]:
        item["stop"] = u"service_ctl.py?name=" + names[i] + "&cmd=stop"

    print(template.load(u"service_list.html", dct))
  except Exception as e:
    print(u"I/O error: {0}".format( str(e)))
