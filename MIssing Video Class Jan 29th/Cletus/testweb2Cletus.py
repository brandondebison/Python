#!/usr/local/bin/python3

import cgi;
from wsgiref.simple_server import make_server;

html = """
<!DOCTYPE html>
<html>
    <head>
        <title> pyhtml web page </title>
    </head>
    <body>
        <form action="" method="POST">
            <label for="name"> Hello</label>
            <input type="text" name="name" value="" />
            <input type="submit" name="submit" value="Submit" />
        </form>
    </body>
</html>
    """;
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