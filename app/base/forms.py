from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

# login


class LoginForm(FlaskForm):
    username = TextField('Username', id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login',
                             validators=[DataRequired()])
# registration


class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create',
                         validators=[DataRequired()])
    email = TextField('Email', id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create',
                             validators=[DataRequired()])
    gitlab_username = TextField('GitLab Username', id='gitlab_username_create',
                                validators=[DataRequired()])
    token = TextField('GitLab Token', id='token_create',
                      validators=[DataRequired()])
