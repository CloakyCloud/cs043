#use the Simpledb from unit 2 to create a database server called httpdb. httpdb will be a very simple database server that will support the four CRUD operations via HTTP paths and query parameters.
#The response string should report the success or failure of the operation. You can make the database store anything you want, but it does have to support each CRUD operation.


#just follow the example to make simplify
#Name = Value
#Number = Key

import wsgiref.simple_server
import urllib.parse
from lesson2_2.database import Simpledb


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    db = Simpledb('phoneNumbers.txt')

    if path == '/insert':
        print('insert')
        #Test String
        #http://localhost:8000/insert?key=dallan&value=11111111111

        start_response('200 OK', headers)
        parameter = urllib.parse.parse_qs(environ['QUERY_STRING'])
        print(parameter)
        name = str(parameter['key'][0])
        number = str(parameter['value'][0])

        db.insert(name, number)
        return ['Inserted'.encode()]




    elif path == '/select':

        #Test String
        #http://localhost:8000/select?key=dallan

        print('find')
        s = db.search_for(params['key'][0])
        start_response('200 OK', headers)
        if s:
            return [s.encode()]
        else:
            return ['NULL'.encode()]


    elif path == '/delete':
        print('delete')
        #Test String
        #http://localhost:8000/delete?key=dallan

        start_response('200 OK', headers)
        parameter = urllib.parse.parse_qs(environ['QUERY_STRING'])
        name = str(parameter['key'][0])

        db.delete_selected(name)
        return ['Deleted'.encode()]



    elif path == '/update':
        print('update')

        #Test string
        #http://localhost:8000/update?key=dallan&value=9999999999


        start_response('200 OK', headers)
        parameter = urllib.parse.parse_qs(environ['QUERY_STRING'])
        print(parameter)
        oldName = str(parameter['key'][0])
        newNumber = str(parameter['value'][0])
        db.edit_selected(oldName, newNumber)

        return['Updated'.encode()]







    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
