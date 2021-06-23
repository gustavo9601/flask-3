from flask import Flask, request
from common import config

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Master Code GM</h1>"


def other_route():
    return "<p>Other route :)</p>"


def saludo(name):
    return f"Hola que tal {name}?"


def suma(valor_1: int, valor_2: int):
    return f"La suma de los valores es: {valor_1 + valor_2}"

def params_url():
    # request.args // get query string ?key=value as a Dictionary
    params_in_the_url = request.args
    print(f"Param key= {params_in_the_url.get('key', 'Not found key :(')}")
    return params_in_the_url

"""
Usando decoradores como callbacks antes y despues de una peticion
"""
@app.before_request
def before_request():
    print('Antes de la peticion....')

@app.route('/callback_intermedian')
def callback_intermedian():
    print('En el callback intermedio...')
    return "Mira la consola >>> :d"

@app.after_request
def before_request(response):
    print('Despues de la peticion...')
    return response

if __name__ == '__main__':
    # Define route like routes laravel
    app.add_url_rule('/other-route', view_func=other_route)
    app.add_url_rule('/config', view_func=config)
    app.add_url_rule('/params_url', view_func=params_url)
    app.add_url_rule('/saludo/<name>', view_func=saludo, methods=['GET'])
    app.add_url_rule('/suma/<int:valor_1>/<int:valor_2>', view_func=suma, methods=['GET'])

    # Execute flask
    """
        debug=True,
        port=5000
    """
    app.run(
        debug=True,
        port=5000
    )
