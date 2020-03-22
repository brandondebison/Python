#!/usr/local/bin/python3
import cgitb 
cgitb.enable()
import cgi

import xml.etree.ElementTree as etree 
from wsgiref.simple_server import make_server

tree = etree.parse('fav_movies.xml')

root = tree.getroot()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title> XML Movies</title>
        <style> th { padding: 25px; margin-top: 75px; border: 1px solid black;} </style>
    </head>
    <body>
    </div>
    <table style="border: 2px solid black;">
    
    
"""
counter = 0
html += "<tr>"

for node in root:
    elementName = node.tag
    elementAttribute = node.attrib
    i = 0


    for elementTag, elementTagValue in elementAttribute.items():

        for item in node:
            itemAttribute = item.tag 
            itemValue = item.text
            if str(itemAttribute) == "Picture":
                tempPicture = str(itemValue)
            elif str(itemAttribute) == "Title":
                tempTitle = str(itemValue)
            elif str(itemAttribute) == "Year":
                tempYear = str(itemValue)
            elif str(itemAttribute) == "Director":
                tempDirector = str(itemValue)
            elif str(itemAttribute) == "MainActor":
                tempMainActor = str(itemValue)
            elif str(itemAttribute) == "Genre":
                tempGenre = str(itemValue)

        html += "<th><h1><img src="+tempPicture+"><br/>Title: "+tempTitle+" ("+tempYear+")</h1><br/>"
        html += "Director: "+tempDirector+"<br/>"
        html += "Main Actor / Actress: "+tempMainActor+"<br/>"
        html += "Genre: "+tempGenre+"<br/></th>"

        counter += 1
        
        if (counter % 3) == 0:
            html += "</tr><tr>"
            
html += "</table></div></body></html>"

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