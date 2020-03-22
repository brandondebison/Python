#!/usr/local/bin/python3
import cgitb 
cgitb.enable()
import cgi
import MySQLdb
import MySQLdb.cursors;

from wsgiref.simple_server import make_server

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='student',
    passwd='student',
    db='assignment3',
    cursorclass=MySQLdb.cursors.DictCursor
) 

cursor = db.cursor()

cursor.execute("SELECT * FROM registered_users")
data = cursor.fetchall()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title> Records Form  </title>
    </head>
    <body>
    <table border=1>
    <tr>
        <th>Id</th>
        <th>First Name</th>
        <th>Last Name</th>

    </tr>
    
"""
user_array = []
all_users = []

for row in data:
    id = row["user_id"]
    firstName = row["firstName"]
    lastName = row["lastName"]
    user_array = [str(id),firstName,lastName]
    all_users.append(user_array)

for i in range (0,len(all_users)):
    html += "<tr>"
    for j in range (0,len(all_users[0])):

        item = all_users[i][j]
        html +="<td>" +str(item) + "</td>"

    html += "</tr>"


html += "</table></body></html>"

def app (environ, start_response):
    response =html;
    if (environ['REQUEST_METHOD'] == "POST"):
        post_env = environ.copy();
        post_env["QUERY_STRING"] = "";

        post = cgi.FieldStorage(
            fp = environ["wsgi.input"],
            environ = post_env,
            keep_blank_values=True
        );

        nameVar = post["name"].value;
        response = 'Thanks %s. You pressed submit ' % nameVar;

    start_response('200 OK', [('Content-Type', 'text/html')]);
    return [response.encode( )];

if __name__ =='__main__':
    try:
        from wsgiref.simple_server import make_server;
        httpd = make_server('',8080,app);
        print('Serving on port 8080...');
        httpd.serve_forever();
    except KeyboardInterrupt:
        print("Goodbye")