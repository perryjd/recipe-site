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
<link rel="stylesheet" type="text/css" href="test.css">
<link rel="stylesheet" href="dist/css/bootstrap.min.css">
<script src="jquery-2.1.1.min.js"></script>
</head>
<body>
<div class="container-fluid" id="background">
<div class="row">
<div class="col-md-2"></div>
<div class="col-md-8" id="ribbon">
<div class="col-md-6" id="content">
<h1>This is the recipe site!</h1>''')
#grabbing table, making master list. TAKE THIS OUT once done
arguments = cgi.FieldStorage()
db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='recipe_site')
cur = db.cursor()
cur.execute("SELECT * FROM recipes")
print('<table><tr><th>Master List</th></tr>')
rows = cur.fetchall()
for row in rows:
	print ('<tr><td><a href="'+str(row[2])+'" target="_blank">'+str(row[1])+'</a></td></tr>')
print("</table>")
#this is for the random recipe generator
recipeTotal=cur.rowcount
randIndex = random.randrange(1, recipeTotal+1)
for row in rows:
	if (row[0] == randIndex):
		print("<a href='"+str(row[2])+"' target='_blank' class='Random'><div id='randButton'>Random recipe!</div></a>")


#now adding search bar
print('</div>')
print('<div id="searchBox" class="col-md-2">')
print('''<form action="test.py">
	<input type="text" name="search" placeholder="search by ingredient">
	<input type="submit" value="go">
	</form>''')
if ("search" in arguments.keys() != 0):
	query = str(arguments["search"].value)
	cur.execute("SELECT * FROM recipes WHERE name LIKE %s", ("%"+query+"%"))
	rows = cur.fetchall()
	print('<table><tr><th>Search Results</th></tr>')
	for row in rows:
		print ('<tr><td><a href="'+str(row[2])+'" target="_blank">'+str(row[1])+'</a></td></tr>')
	print("</table></div>")
#now adding add-a-recipe feature
print('<div id="addRecipe">')
print('<h3>Add your recipe to the database!</h2>')
print('<form action="test.py">')
print('<p><input type="text" name="newName" placeholder="your recipe\'s name"></p>')
print('<p><input type "text" name="newUrl" placeholder="your recipe\'s URL"></p>')
print('<p><input type="submit" value="submit!"></p>')
print('</form>')
if (("newName" in arguments.keys() != 0) and ("newUrl" in arguments.keys() != 0)):
	newName = str(arguments["newName"].value)
	newUrl = str(arguments["newUrl"].value)
	cur.execute("INSERT INTO recipes (name, url) VALUES (%s,%s);", ("'"+newName+"'", "'"+newUrl+"'"))

print('</div>')
print('''
<div class="col-md-2"></div>
</div>
</div>
</body>
</html>''')

