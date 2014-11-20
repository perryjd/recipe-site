#!/usr/bin/env python
 # -*- coding: UTF-8 -*-# enable debugging
import cgitb
import cgi
import MySQLdb

cgitb.enable()
print("Content-Type: text/html;charset=utf-8\n")
print('''<html>
<head>
<title>TEST PAGE</title>
</head>
<body>
<p> <a href='http://www.reddit.com'><img src='http://www.bordercolliedog.org/wp-content/uploads/bordercolliedog4-300x265.jpg' /> </a></p>
<p>See that dog? It's a border collie.</p><p>We'll name him Kevin, after English long-distance runner <a href='http://en.wikipedia.org/wiki/Kevin_Forster'>Kevin Forster</a>.</p><p> Kevin, the border collie, would like to take you to Reddit.</p>
''')
arguments = cgi.FieldStorage()
db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='recipe_site')
cur = db.cursor()
cur.execute("SELECT * FROM recipes")
print("<table><tr><th>Recipe Name</th><th>Recipe URL</th></tr>")
for row in cur.fetchall():
	#i think adding a link goes here???
	print ("<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td></tr>")
print("</table>")
if ("num" in arguments.keys()):
	limit = int(arguments["num"].value)
else:
	limit = 0


i = 0
while (i < limit):
	print ('''<p>This is a test!</p>''')
	i += 1

print('''
</body>
</html>''')
