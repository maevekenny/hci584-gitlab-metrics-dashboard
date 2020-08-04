from flask import Blueprint

"""
HCI 584 - Summer 2020
The basae_blueprint module.

Author: Maeve Kenny
"""

blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)
