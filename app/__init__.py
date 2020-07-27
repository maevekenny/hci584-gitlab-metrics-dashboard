from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    """Database registration"""
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    """Home / base site blueprint initialization"""
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    """Database configuration"""

    @app.before_first_request
    def initialize_database():
        """Database initialization with table creation"""
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        """Database shut down"""
        db.session.remove()


def configure_logs(app):
    """Soft logging configuration"""
    try:
        basicConfig(filename='error.log', level=INFO)
        logger = getLogger()
        logger.addHandler(StreamHandler())
    except:
        pass


def create_app(config, selenium=False):
    """App initialization with database / blueprints configuration"""
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)
    return app
