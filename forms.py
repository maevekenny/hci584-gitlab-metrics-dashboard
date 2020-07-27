from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(Form):
    """ 
    This is a class for the Registration Form.

    Attributes: 
        Form (Form): The flask_wtf Form class.
    """
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    gitlab_username = TextField(
        'GitLab Username', validators=[DataRequired(), Length(min=6, max=40)])
    token = TextField(
        'GitLab Token', validators=[DataRequired(), Length(min=6, max=40)])

    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
         EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    """ 
    This is a class for the Login Form.

    Attributes: 
        Form (Form): The flask_wtf Form class.
    """
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    """
    This is a class for the Forgot Email Form.

    Attributes:
        Form (Form): The flask_wtf Form class.
    """
    email = TextField('Email', validators=[
                      DataRequired(), Length(min=6, max=40)])
