from flask import Blueprint

"""
HCI 584 - Summer 2020
The home_blueprint module.

Author: Maeve Kenny
"""
blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)
