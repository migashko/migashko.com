#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess

html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
        <title>без имени</title>
        <meta http-equiv="content-type" content="text/html;charset=utf-8"/>
        <meta name="generator" content="Geany 1.24.1"/>
</head>

<body>
<div>mediacenter:</div><div>{{mediacenter}}</div>
<div>mpd:</div><div>{{mpd}}</div>
<div>transmission-daemon:</div><div>{{transmission-daemon}}</div>
</body>
</html>'''

bashCommand = 'ps -A'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

mediacenter = "OFF"
if "mediacenter" in output.split():
  mediacenter = "ON"

mpd = "OFF"
if "mpd" in output.split():
  mpd = "ON"

transmission_daemon = "OFF"
if "transmission-da" in output.split():
  transmission_daemon = "ON"

html = html.replace("{{mediacenter}}",mediacenter)
html = html.replace("{{mpd}}",mpd)
html = html.replace("{{transmission-daemon}}",transmission_daemon)

print(html) 



