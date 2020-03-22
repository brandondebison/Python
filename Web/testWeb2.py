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
            <label for="name"> Name 1</label>
            <input type="text" name="name1" value="" /><br/>
            <label for="name"> Name 2</label>
            <input type="text" name="name2" value="" /><br/>
            <label for="name"> Name 3</label>
            <input type="text" name="name3" value="" /><br/>
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

        name1 = post["name1"].value;
        name2 = post["name2"].value;
        name3 = post["name3"].value;

        e1 = "<span style='color:red'>*required </span>"
        e2 = "<span style='color:red'>*required</span>"
        e3 = "<span style='color:red'>*required</span>"

        if(name1 ==""):
            errors = 1
        else:
            e1=""
        if(name2 ==""):
            errors = 2
        else:
            e2=""

        if(name3 ==""):
            errors = 3
        else:
            e3=""

        if (errors != 0):
            response2 = """
            <!DOCTYPE html>
            <html>
                <head>
                    <title> pyhtml web page </title>
                </head>
                <body>
                    <form action="" method="POST">
                        <label for="name"> Name 1</label>
                        <input type="text" name="name1" value="" />%s <br/>
                        <label for="name"> Name 2</label>
                        <input type="text" name="name2" value="" />%s<br/>
                        <label for="name"> Name 3</label>
                        <input type="text" name="name3" value="" />%s<br/>
                        <input type="submit" name="submit" value="Submit" />
                    </form>
                </body>
            </html>
            """


        response = response2 % (e1,e2,e3);




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