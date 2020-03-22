#!/usr/bin/python3

import cgi;
from wsgiref.simple_server import make_server;

html = """
        <!DOCTYPE html>
        <html
            <head>
                <title>pyhtml web page</title>
            </head>

            <body>
                <form action="" method="POST">
                    <label for="name">Name 1</label>
                    <input type="text"  name="name" value="" />
                    <label for="name">Name 2</label>
                    <input type="text"  name="name" value="" />
                    <label for="name">Name 3</label>
                    <input type="text"  name="name" value="" />
                    <label for="name">Name 4</label>
                    <input type="text"  name="name" value="" />
                    <input type="submit"  name="submit" value="Submit" />
            </body>

        </html>
        """;
def app (environ, start_response):
    response = html;
    if ( environ['REQUEST_METHOD'] == "POST"):
        post_env = environ.copy();
        post_env["QUERY_STRING"] = "";

        post = cgi.FieldStorage(
            fp = environ["wsgi.in"],
            environ = post_env,
            keep_blank_values=True
        );

        nameVar = post["name"].value;
        #response = 'Thanks %s. You pressed submit' % nameVar;
        e1 = "<span style ='color:red'>*required";
        e2 = "<span style ='color:red'>*required";
        e3 = "<span style ='color:red'>*required";
        e4 = "<span style ='color:red'>*required";


    if (name1==""):
        errors = 1;
    else:
            e1 = "";

    if (errors != 0):
        response = """
        <!DOCTYPE html>
        <html
            <head>
                <title>pyhtml web page</title>
            </head>

            <body>
                <form action="" method="POST">
                    <label for="name">Name 1</label>
                    <input type="text"  name="name" value="" />%s
                    <label for="name">Name 2</label>
                    <input type="text"  name="name" value="" />%s
                    <label for="name">Name 3</label>
                    <input type="text"  name="name" value="" />%s
                    <label for="name">Name 4</label>
                    <input type="text"  name="name" value="" />%s
                    <input type="submit"  name="submit" value="Submit" />
            </body>

        </html>
        """;


    start_response('200 OK', [('Content-Type','text/html')]);
    return [response.encode( )];

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server;
        httpd = make_server('', 8080, app);
        print('Serving on port 8080...');
        httpd.serve_forever();
    except KeyboardInterrupt:
        print("K bye");