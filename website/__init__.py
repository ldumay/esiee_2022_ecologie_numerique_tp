from flask import Flask


def create_app():
    app = Flask(__name__)

    # secret key for cookies
    app.config['SECRET_KEY'] = 'dnjqkndkjsndjksqshfibvdhhjbsui'

    from .views import views

    # the root inside the url locate the methode inside the views.py
    app.register_blueprint(views, url_prefix='/')

    return app
