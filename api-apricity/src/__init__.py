from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from configuration import config
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    cors.init_app(app)
    from app import api
    api.init_app(app)
    return app
