#create a web app that returns the string "Good morning, Sunshine!" (Lesson 3)

import wsgiref.simple_server

def test_app(envrion, start_response):
    status = '200 OK'
    headers = [('Contetent-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    return['"Good morning, Sunshine!"'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, test_app)
print("Serving on port 8000....")

httpd.serve_forever()