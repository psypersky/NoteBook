# WSGI

## History

Web servers in the beginning used to seve only static files

Users -> [Webserver -> Files]

There was no sessions, form, dinamic views

CGI Common Gateway interface (Invoke a script for dynamic content) was born, instead of service a file you would invoke a script

WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.

WSGI is a Python standard described in detail in PEP 3333.

[Servers which support WSGI](https://wsgi.readthedocs.io/en/latest/servers.html)

[Frameworks that run on WSGI](https://wsgi.readthedocs.io/en/latest/frameworks.html)

A WSGI server (meaning WSGI compliant) only receives the request from the client, pass it to the application and then send the response returned by the application to the client. It does nothing else. All the gory details must be supplied by the application or middleware.

WSGI for Web Developers (Ryan Wilson-Perkin) https://www.youtube.com/watch?v=WqrCnVAkLIo

TODO:

- Create a WSGI server
- Create a WSGI application
- Describe how gunicorn works internally
