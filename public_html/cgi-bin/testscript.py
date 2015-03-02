#!/usr/local/nin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FiledStorage()

print "Content-Type: text/html"         #html is following 
print                                   # blank line means end of headers 
print "<html><head><TITLE>CGI Script Output</TITLE></head>"
print "<body><H1>Form Values</H1>"
print "<table><tr><th>Key</th></tr>"

if 'name' in form: 
  print "<tr><td>name</td><td>%s</td></tr>"% form['name'].value
else:
  print "name not fount"
print "<table>"

print "</body></html>"
