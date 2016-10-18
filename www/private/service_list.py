#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

import os, sys
from genshi.template import TemplateLoader
from genshi.output import encode, get_serializer
import codecs
import subprocess

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

loader = TemplateLoader(
    os.path.join(os.path.dirname(__file__), '.'),
    auto_reload=True
)

def run_program(cmd):
  ret = u""
  PIPE = subprocess.PIPE
  p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        stderr=subprocess.STDOUT, close_fds=True)
  while True:
    s = p.stdout.readline()
    if not s: break
    ret = ret + s.decode("utf-8") + u"\n"
  return ret;

def get_service_status(name):
  return run_program("systemctl is-active " + name)

import getpass
getpass.getuser()

if __name__ == '__main__':
  try:
#    print( getpass.getuser() )
    names=["mpd", "transmission", "mediacenter", "lighttpd"]
    services=[]
    for i in range(len(names)):
      services.append({})
      services[i]["name"]=names[i]
      services[i]["status"]=get_service_status(names[i])
    tmpl = loader.load(u"service_list.tpl", encoding="utf-8")
    stream = tmpl.generate(services=services)
    rend = stream.render(encoding="utf-8")
    s = rend.decode("utf-8")
    print(s)
  except Exception as e:
    print(u"I/O error: {0}".format( str(e)))
