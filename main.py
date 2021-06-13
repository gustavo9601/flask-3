from flask import Flask, request, make_response, redirect
from common import config

"""
execute in console

export FLASK_APP=current_name_file_init.py => export || set
export FLASK_DEBUG=1 => export || set
flask run
"""
settings = config()['settings']

# Init app
app = Flask(settings['app_name'])


@app.route('/hello-world')
def hello_world():
    return "Hi I'm the besst developer IA and ML in the World"

@app.route('/ip_user')
def get_ip_form_cookie():
    user_ip = request.cookies.get('user_ip') if  request.cookies.get('user_ip') else get_ip_client()
    return f"Your IP is {user_ip}"

@app.route('/')
def index():
    user_ip = get_ip_client()
    # create a response to control
    # and redirect to other path
    response = make_response((redirect('/hello-world')))
    # making acookir in the browser
    response.set_cookie('user_ip', user_ip)

    return response


def get_ip_client():
    return request.remote_addr