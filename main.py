from flask_migrate import Migrate
from os import environ
from sys import exit

from config import config_dict
from app import create_app, db

"""
HCI 584 - Summer 2020
The root module to build and run the GitLab Metrics Dashboard.
The code for this project can be found at https://github.com/maevekenny/hci584-gitlab-metrics-dashboard.

Author: Maeve Kenny
"""
get_config_mode = environ.get('CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid config environment variable entry.')

app = create_app(config_mode)
Migrate(app, db)

if __name__ == "__main__":
    """
    The main initialization of the app to run.
    """
    app.run()
