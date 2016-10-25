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

def load(path, dct):
  tmpl = loader.load(path, encoding="utf-8")
  stream = tmpl.generate(g=dct)
  rend = stream.render(encoding="utf-8")
  s = rend.decode("utf-8")
  return s;
