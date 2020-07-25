import os
from os import environ


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'key'

    # Creates file in the root directory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'database.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # SQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('DATABASE_USER', 'test-user'),
        environ.get('DATABASE_PASSWORD', 'password'),
        environ.get('DATABASE_HOST', 'db'),
        environ.get('DATABASE_PORT', 5432),
        environ.get('DATABASE_NAME', 'gitlab-dashboard')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
