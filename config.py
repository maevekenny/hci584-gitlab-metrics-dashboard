import os
from os import environ

"""
HCI 584 - Summer 2020
The module that holds the configuration (debug / production) classes.

Author: Maeve Kenny
"""


class Config(object):
    """ 
    This is a class for a config object.

    Attributes: 
        object (object): The config object
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'key'

    # Creates file in the root directory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'database.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    This is a class for the production config.

    Attributes:
        Config (Config): The config object
    """
    DEBUG = False

    # Security configuration
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # SQL database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('DATABASE_USER', 'test-user'),
        environ.get('DATABASE_PASSWORD', 'password'),
        environ.get('DATABASE_HOST', 'db'),
        environ.get('DATABASE_PORT', 5432),
        environ.get('DATABASE_NAME', 'gitlab-dashboard')
    )


class DebugConfig(Config):
    """
    This is a class for the debug config.

    Attributes:
        Config (Config): The config object
    """
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
