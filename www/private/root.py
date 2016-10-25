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

def status(name):
  res = run_program("systemctl is-active " + name)
  res = res.replace('\n','')
  return res

def restart(name):
  res = run_program("sudo systemctl restart " + name)
  res = res.replace('\n','')
  return res
