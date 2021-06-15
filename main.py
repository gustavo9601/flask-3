from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from common import config
from flask_bootstrap import Bootstrap
# import libreries to use forms
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# import librerias para pruebas
import unittest

"""
execute in console

export FLASK_APP=current_name_file_init.py => export || set
export FLASK_DEBUG=1 => export || set
export FLASK_ENV=development => export || set
flask run

echo FLASK_ENV=development // se puede imprimir el valor de la variable por consola
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
# .config['SECRET_KEY'] // generando el tocken de encriptacion para la sesiones en flask

app.config['SECRET_KEY'] = settings['secret_key']
app.config['WTF_CSRF_ENABLED'] = False

# Init bootstrap plugin flask
bootstrap = Bootstrap(app)


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
    # making a session encrypted
    session['user_ip'] = user_ip

    return response


class LoginForm(FlaskForm):
    # Usando las propias clases de Flask para generar el formulario
    # DataRequired // validacion de campos requeridos
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.route('/form-login', methods=['GET', 'POST'])
def form_login():
    login_form = LoginForm()
    # session.get('username') // obteniendo valores de la session encriptada
    username = session.get('username') if session.get('username') else None

    context = {
        'login_form': login_form,
        'username': username
    }

    if request.method == 'POST' and login_form.validate_on_submit():
        # Obteniendo valores enviados
        username = login_form.username.data
        session['username'] = username

        # Creando un mensaje flash
        flash('Nombre de usuario se registro en la sesion :)')

        return redirect(url_for('form_login'))

    return render_template('form-login.html', **context)


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


"""
Commands in console
"""
@app.cli.command()
def test():
    # desde consola flask test
    # flask name_function

    # Especificando el directorio donde debe buscar los test
    tests = unittest.TestLoader().discover('./tests')
    # todos los archivos debeb empexar por test_{name_test}.py
    # Ejecutando todos los test encontrados en el directorio anterior
    unittest.TextTestRunner().run(tests)