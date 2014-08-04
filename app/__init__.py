# coding=utf-8

from flask import Flask
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('../config.py')

    bootstrap.init_app(_app)

    from views import main as main_bp
    _app.register_blueprint(main_bp)

    return _app

from views import *
