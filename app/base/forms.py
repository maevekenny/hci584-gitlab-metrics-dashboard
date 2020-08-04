from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

"""
HCI 584 - Summer 2020
The module that holds the two unique Form types for the system.

Author: Maeve Kenny
"""


class LoginForm(FlaskForm):
    """
    The function to create the login form.

    Attributes:
        FlaskForm (Form): The form data to build the login form

    """
    username = TextField('Username', id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    """
    The function to create the account registration form.

    Attributes:
        FlaskForm (Form): The form data to build the registration form

    """
    username = TextField('Username', id='username_create',
                         validators=[DataRequired()])
    email = TextField('Email', id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create',
                             validators=[DataRequired()])
    gitlab_username = TextField('GitLab Username', id='gitlab_username_create',
                                validators=[DataRequired()], default='maevekenny210')
    token = TextField('GitLab Token', id='token_create',
                      validators=[DataRequired()], default='pLey582NjxGWUAw5FccS')
