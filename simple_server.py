#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

'''
return
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import os
 
os.chdir("./www")
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)

 
httpd = server(server_address, handler)
httpd.serve_forever()
'''
 
import http.server
import socketserver
import os

PORT = 8001
os.chdir("./www")

handler = http.server.SimpleHTTPRequestHandler
handler.cgi_directories = ["/private"]
httpd = socketserver.TCPServer(("0.0.0.0", PORT), handler)
httpd.server_name = "vova"
httpd.server_port = PORT
print("serving at port", PORT)
httpd.serve_forever()

