"""Route introduction: static and dynamic."""
from bottle import run, route


@route('/')
def index():
    """Static Route."""
    return '<h1>Live python</h1>'


@route('/<person>')
def index_test(person):
    """Dynamic Route for test."""
    if person == 'Charles':
        return 'You are the best x-man'
    return '<h1>hello {}</h1>'.format(person)


run(port=8080)
