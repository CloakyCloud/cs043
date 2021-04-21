import wsgiref.simple_server
import http.cookies


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8'),
               ('Set-Cookie', 'session=dallan; expires=Sun, 25 Dec 2016 00:15:49 GMT'.format(counter)),
               ('Set-Cookie', 'weight=140'),
               ('Set-Cookie', 'shoe_size=10')

    #Set cookies here inside the headers

]
    start_response('200 OK', headers)

    if 'HTTP_COOKIE' in environ:
        #print(environ['HTTP_COOKIE'])
        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        res = ''
        for key in cookies:
            res += (key + ": " + cookies[key].value +"\n")
        return[res.encode()]

    #Cookie parser goes here . . .


httpd = wsgiref.simple_server.make_server('', 8000, application)

print("Serving on port 8000...")

httpd.serve_forever()