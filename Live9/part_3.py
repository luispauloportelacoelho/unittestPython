from bottle import request, route, run, response


@route('/')
def hello_again():
    if request.get_cookie('visited'):
        return 'Hello, welcome'
    response.set_cookie('visited', 'yes')
    return 'Hello it is a pleasure to meet you'


run(port=8080)
