from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

"""
HCI 584 - Summer 2020
The module to do all system / database / blueprint configuration. The app is registered and created in this module.

Author: Maeve Kenny
"""

db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    """
    Database registration

    Attributes:
        app (Flask): The main application

    """
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    """
    Home / base site blueprint initialization

    Attributes:
        app (Flask): The main application

    """
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    """
    The function for database configuration.

    Attributes:
        app (Flask): The main application

    """
    @app.before_first_request
    def initialize_database():
        """
        The function for database initialization with table creation

        """
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        """
        The function for shutting down the database.
        """
        db.session.remove()


def configure_logs(app):
    """
    The function for soft logging configuration.

    Attributes:
        app (Flask): The main application

    """
    try:
        basicConfig(filename='error.log', level=INFO)
        logger = getLogger()
        logger.addHandler(StreamHandler())
    except:
        pass


def create_app(config):
    """
    App initialization with database / blueprints configuration

    Attributes:
        config (config): The configuration file to pass in
    """
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)
    return app
