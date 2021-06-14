from flask import Flask, request, make_response, redirect, render_template
from common import config

"""
execute in console

export FLASK_APP=current_name_file_init.py => export || set
export FLASK_DEBUG=1 => export || set
flask run
"""
settings = config()['settings']

# Init app

"""
template_folder // define the templaste html folder
static_folder // define the media content
"""
app = Flask(
    settings['app_name'],
    template_folder='./templates',
    static_folder='./static'
)



@app.route('/hello-template')
def hello_template():
    context = {
        'greeting': 'Hello template',
        'values': [1, 2, 3, 4, 56]
    }
    # Pass params to template
    # **context // devuelve todos los valores del diccionario como variable independientes
    return render_template('hello.html', **context)


@app.route('/hello-world')
def hello_world():
    return "Hi I'm the besst developer IA and ML in the World"


@app.route('/ip_user')
def get_ip_form_cookie():
    user_ip = request.cookies.get('user_ip') if request.cookies.get('user_ip') else get_ip_client()
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

"""
Handling errors 
"""
@app.errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def error_500(error):
  return render_template('500.html')
