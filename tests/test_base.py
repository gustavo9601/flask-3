from flask_testing import TestCase
# Libreria que devuelve el estado actual de la app
from flask import current_app, url_for

# Importando la app configurada de flask
from main import app


class MainTest(TestCase):

    def create_app(self):
        # Habilitando el testing en la configuracion de flask
        app.config['TESTING'] = True
        # Inhabilitando el CSRF de los form ya que no hay sessiones activas del usuario
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        # Verificando que existe la app
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        # Verificando que este en modo testing
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirect_to_hello_world(self):
        # .client.get(url_for('index')) // obtenido la ruta para la funcion index
        url_index = self.client.get(url_for('index'))

        # verificando que la ruta inicial index, sea redirigida a hello_world
        self.assertTrue(url_index, url_for('hello_world'))

    def test_check_status_code_form_login_url(self):
        response = self.client.get(url_for('form_login'))
        self.assert200(response)

    def test_post_login_form(self):
        mock_user = {
            'username': 'gus',
            'password': 'test-password'
        }
        # data= // permite enviar datos al request
        # .post // cambiando el metodo
        response = self.client.post(url_for('form_login'), data=mock_user)
        # verifica que luego de la peticion halla sido redigido a la funcion enviada por param
        self.assertRedirects(response, url_for('form_login'))
