#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

import os, sys
import codecs
import subprocess
import template

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

def reboot():
  res = run_program("sudo /sbin/shutdown -r 1")
  return res

def status(name):
  res = run_program("sudo /bin/systemctl is-active " + name)
  res = res.replace('\n','')
  return res

def restart(name):
  res = run_program("sudo /bin/systemctl restart " + name)
  res = res.replace('\n','')
  return res

def start(name):
  res = run_program("sudo /bin/systemctl start " + name)
  res = res.replace('\n','')
  return res

def stop(name):
  res = run_program("sudo /bin/systemctl stop " + name)
  res = res.replace('\n','')
  return res

def run_du(path):
  res = run_program("sudo /usr/bin/du -h --max-depth=1 " + path + " | sort -n");
  return res



