"""
Copyright (c) 2016, BRCK Inc
All Rights Reserved
"""
import os

from flask import Flask, session
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


db = SQLAlchemy()

def create_app(config_name):
    """Creates the Flash application object

    :rtype Flask The application object
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    CORS(app)


    # Import and register the Blueprints
    from views import moja

    app.register_blueprint(moja)
    return app
