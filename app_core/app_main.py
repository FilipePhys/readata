from flask import Flask
from app_core import frontend
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
frontend.init_app(app)

db = SQLAlchemy(app)
