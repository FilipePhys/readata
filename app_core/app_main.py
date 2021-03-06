import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'frontend', 'templates')  # Put this outside

app = Flask(__name__, template_folder=template_dir)
app.config.from_object('config')
db = SQLAlchemy(app)

from app_core import frontend, api

frontend.init_app(app)
api.init_app(app)

