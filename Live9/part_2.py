from bottle import get, post, run, request


@get('/')
def index_get():
    return '''
    <form action="/" method="post">
        Username: <input name="username" type="text" />
        </br>
        Password: <input name="password" type="password" />
        </br>
        <input value="Login" type="submit" />
    </form>'''


@post('/')
def index_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return '''
    <h1> Your informations</h1>
    </br>
    <h4>{}</h4>
    <h4>{}</h4>'''.format(username, password)


#run(port=8080)
