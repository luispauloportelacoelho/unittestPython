from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Ola Live'


@app.route('/live')
def live_page():
    return 'Estamos online'


app.run()
