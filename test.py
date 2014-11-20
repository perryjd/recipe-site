#!/usr/bin/env python
 # -*- coding: UTF-8 -*-# enable debugging
import cgitb
import cgi
import MySQLdb
import random

cgitb.enable()
print("Content-Type: text/html;charset=utf-8\n")
print('''<html>
<head>
<title>TEST PAGE</title>
</head>
<body>
<p>This is the recipe site!</p>''')
arguments = cgi.FieldStorage()
db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='recipe_site')
cur = db.cursor()
cur.execute("SELECT * FROM recipes")
print('<table><tr><th>Recipe Name</th><th>Recipe URL</th></tr>')
rows = cur.fetchall()
for row in rows:
	print ('<tr><td>'+str(row[1])+'</td><td><a href='+str(row[2])+' target="_blank">link</a></td></tr>')
print("</table>")
if ("num" in arguments.keys()):
	limit = int(arguments["num"].value)
else:
	limit = 0
#this is for the random recipe generator
recipeTotal=cur.rowcount
randIndex = random.randrange(1, recipeTotal+1)
for row in rows:
	if (row[0] == randIndex):
		print("<p><a href='"+str(row[2])+"' target='_blank'>Random recipe!</a></p>")

i = 0
while (i < limit):
	print ('''<p>This is a test!</p>''')
	i += 1

print('''
</body>
</html>''')
