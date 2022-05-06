from flask import Flask
from stock_management.ext import dynaconf


def create_app():
    app = Flask(__name__)
    dynaconf.init_app(app)

    @app.route('/')
    def teste():
        return "hello!!"

    return app
