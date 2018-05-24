from bottle import jinja2_view, route, run, request, response


@route('/<area>')
@jinja2_view('paginas/test.html')
def test(area):
    return dict(name=area)


@route('/user', method='GET')
@jinja2_view('paginas/user.html')
def user():
    links = ['home', 'about', 'help']
    return dict(links=links)

run(port=8080)
