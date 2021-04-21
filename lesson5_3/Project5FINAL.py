import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import random

connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if (r == []):
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken <a href="/">Back</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            connection.execute('INSERT INTO users VALUES (?, ?)', [un, pw])
            connection.commit()
            return['Success! You can now sign in as {}. <a href="/">Back to Sign in</a>'.format(un).encode()]




    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['User {} successfully logged in. <a href="/account">Account</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password <a href="/">Back</a>'   .encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)

        if 'HTTP_COOKIE' not in environ:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'session' not in cookies:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()

        print(environ['HTTP_COOKIE'])

        #This is where the game begins. This section of is code only executed if the login form works, and if the user is successfully logged in
        if user:
            correct = 0
            wrong = 0
            # [INSERT CODE FOR COOKIES HERE]
            cookies = http.cookies.SimpleCookie()
            if 'HTTP_COOKIE' in environ:
                if 'correct' in cookies:
                    correct = int(cookies['score'].value.split(':')[0])
                if 'wrong' in cookies:
                    wrong = int(cookies['score'].value)

                    correct = 0
            else:
                correct = 0



            page = '<!DOCTYPE html><html><head><title>Multiply with Score</title></head><body>'
            if 'factor1' in params and 'factor2' in params and 'answer' in params:

                parameter = urllib.parse.parse_qs(environ['QUERY_STRING'])
                f1 = int(parameter['factor1'][0])
                f2 = int(parameter['factor2'][0])
                answer = int(parameter['answer'][0])

                # [INSERT CODE HERE. If the answer is right, show the “correct” message. If it’s wrong, show the “wrong” message.]

                #get score from cookies
                cookies = http.cookies.SimpleCookie()
                cookies.load(environ['HTTP_COOKIE'])
                res = []
                for key in cookies:
                    res.append(key + ':' + cookies[key].value)
                print(res)





                if f1 * f2 == answer:
                    page += '<p style="background-color: lightgreen">Correct, {} X {} = {}</p>'.format(str(f1), str(f2), str(answer).encode())
                    correct = correct + 1
                else:
                    page += '<p style="background-color: red">Incorrect, {} X {} does not = {}</p>'.format(str(f1), str(f2), str(answer).encode())
                    wrong = wrong + 1



            elif 'reset' in params:
                correct = 0
                wrong = 0

            headers.append(('Set-Cookie', 'correct={}'.format(correct, wrong)))
            headers.append(('Set-Cookie', 'wrong={}'.format(correct, wrong)))

            f1 = random.randrange(10) + 1
            f2 = random.randrange(10) + 1

            page = page + '<h1>What is {} x {}</h1>'.format(f1, f2)

            #[INSERT CODE HERE. Create a list that stores f1*f2 (the right answer) and 3 other random answers]
            #random.shuffle(answer)

            choices = []

            answer = f1 * f2
            choices.append(str(answer))

            top = answer + 20
            bottom = answer - 10

            w1 = random.randrange(bottom, top) + 1
            w2 = random.randrange(bottom, top) + 1
            w3 = random.randrange(bottom, top) + 1

            while w1 == answer:
                w1 = random.randrange(bottom, top) + 1
                if w1 != answer:
                    break
            while w2 == answer:
                w2 = random.randrange(bottom, top) + 1
                if w2 != answer:
                    break
            while w3 == answer:
                w3 = random.randrange(bottom, top) + 1
                if w3 != answer:
                    break

            choices.append(str(w1))
            choices.append(str(w2))
            choices.append(str(w3))

            random.shuffle(choices)
            print(choices)
            one = choices[0]
            two = choices[1]
            three = choices[2]
            four = choices[3]

            hyperlink = '<a href="/account?username={}&amp;password={}&amp;factor1={}&amp;factor2={}&amp;answer={}">{}: {}</a><br>'

            #[INSERT CODE HERE. Create the 4 answer hyperlinks here using string formatting.]

            page = page + hyperlink.format(un, pw, str(f1), str(f2), str(one), 'A', str(one))
            page = page + hyperlink.format(un, pw, str(f1), str(f2), str(two), 'B', str(two))
            page = page + hyperlink.format(un, pw, str(f1), str(f2), str(three), 'C', str(three))
            page = page + hyperlink.format(un, pw, str(f1), str(f2), str(four), 'D', str(four))


            page += '''<h2>Score</h2>
            Correct: {}<br>
            Wrong: {}<br>
            <a href="/account?reset=true">Reset</a>
            </body></html>'''.format(correct, wrong)

            return [page.encode()]
        else:
            return ['Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/':
        page = '''<!DOCTYPE html>
                   <html>
                   <head><title>Sign In</title></head>
                   <body>
                   <form action="/login" style="background-color:gold">
                   <h1>Sign in</h1>
                       Username <input type="text" name="username"><br>
                       Password <input type="text" name="password"><br>
                       <input type="submit" value="Log In">
                   </form>
                   <form action="/register" style="background-color:gold">
                   <h1>New around here?</h1>
                       Username <input type="text" name="username"><br>
                       Password <input type="text" name="password"><br>
                       <input type="submit" value="Register New Account">
                   </form>
                   </body></html>'''

        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return [page.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()