#!/usr/local/bin/python3

import cgi;
from wsgiref.simple_server import make_server;

html = """
    <B> This is my html!!!</B>
    """;

def app (environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')]);
    return [html.encode( )];

if __name__ =='__main__':
    try:
        from wsgiref.simple_server import make_server;
        httpd = make_server('',8080,app);
        print('Serving on port 8080...');
        httpd.serve_forever();
    except KeyboardInterrupt:
        print("Goodbye")