from flask import Flask
from app_core import frontend
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    frontend.init_app(app)

    return app
