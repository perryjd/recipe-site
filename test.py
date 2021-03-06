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
	print ('<tr><td><a href="'+str(row[2])+'" target="_blank">'+str(row[1])+'''</a></td><td>
		<form action="test.py"><input type="hidden" name="toDelete" value="'''+str(row[2])+
		'"><input type="submit" value="delete"></form></td></tr>')
print("</table>")
recipeTotal=cur.rowcount
randIndex = random.randrange(1, recipeTotal+1)
for row in rows:
	if (row[0] == randIndex):
		print("<a href='"+str(row[2])+"' target='_blank' class='Random'><div id='randButton'>Random recipe!</div></a>")
#add recipe feature
if (("newName" in arguments.keys() != 0) and ("newUrl" in arguments.keys() != 0)):
	newName = str(arguments["newName"].value)
	newUrl = str(arguments["newUrl"].value)
	cur.execute("SELECT COUNT(url) FROM recipes WHERE url=%s", (newUrl))
	isSubmitted = cur.fetchone()
	if (isSubmitted[0] == 0):
		cur.execute("INSERT INTO recipes (`ID`, `name`, `url`) VALUES (NULL, %s,%s)", (newName, newUrl))
		db.commit()
		print("""<script>
			alert("Your recipe has been added!");
			</script>""")
	else:
		print("""<script>
			alert("Oops! Someone's added your recipe in the past!");
			</script>""")
elif (("newName" in arguments.keys()) != ("newUrl" in arguments.keys())):
	print("""<script>
		alert("Oops! Please enter both a name and a URL.");
		</script>""")
#delete recipe feature
if ("toDelete" in arguments.keys() != 0):
	hitUrl = str(arguments["toDelete"].value)
	cur.execute("DELETE FROM recipes WHERE url=%s", hitUrl)
	db.commit()
#search feature
if ("search" in arguments.keys() != 0):
	query = str(arguments["search"].value)
	cur.execute("SELECT * FROM recipes WHERE name LIKE %s", ("%"+query+"%"))
	searchRows = cur.fetchall()
	print('<table><tr><th>Search Results</th></tr>')
	for row in searchRows:
		print ('<tr><td><a href="'+str(row[2])+'" target="_blank">'+str(row[1])+'</a></td></tr>')
	print("</table></div>")
print('</div>')
print('<div id="searchBox" class="col-md-2">')
print('''<form action="test.py">
	<input type="text" name="search" placeholder="search by ingredient">
	<input type="submit" value="go">
	</form>''')
print('<div id="addRecipe">')
print('<h3>Add your recipe to the database!</h2>')
print('<form action="test.py">')
print('<p><input type="text" name="newName" placeholder="your recipe\'s name"></p>')
print('<p><input type "text" name="newUrl" placeholder="your recipe\'s URL"></p>')
print('<p><input type="submit" value="submit!"></p>')
print('</form>')
print('</div>')
print('''
<div class="col-md-2"></div>
</div>
</div>
</body>
</html>''')

