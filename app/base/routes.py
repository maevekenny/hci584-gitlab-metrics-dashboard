from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User
from app.base.util import verify_pass

"""
HCI 584 - Summer 2020
The module that holds the blueprint route configurations.

Author: Maeve Kenny
"""


@blueprint.route('/')
def route_default():
    """
    The function to create the default route.

    Returns:
        Redirection to the base_blueprint
    """
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/error-<error>')
def route_errors(error):
    """
    The function to catch errors when routing.

    Attributes:
        error (string): The particular error

    Returns:
        Redirection to the error templates
    """
    return render_template('errors/{}.html'.format(error))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    The function to route to the login page.

    Returns:
        Redirection to the login templates
    """
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Look up the username
        user = User.query.filter_by(username=username).first()

        # Validate the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))

        # Return error
        return render_template('login/login.html', msg='Wrong user or password', form=login_form)

    if not current_user.is_authenticated:
        return render_template('login/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/create_user', methods=['GET', 'POST'])
def create_user():
    """
    The function to route to the registration form.

    Returns:
        Redirection to the registration templates
    """
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']
        gitlab_username = request.form['gitlab_username']
        token = request.form['token']

        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('login/register.html', msg='Username already registered', form=create_account_form)

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('login/register.html', msg='Email already registered', form=create_account_form)

        # If not, create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('login/register.html', msg='User created <br> please <a href="/login">login</a>', form=create_account_form)

    else:
        return render_template('login/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    """
    The function to log the user out and reroute the login page.

    Returns:
        Redirection to the login page
    """
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@login_manager.unauthorized_handler
def unauthorized_handler():
    """
    The function to route 403 unauthorized template

    Returns:
        Redirection to the error template
    """
    return render_template('errors/403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    """
    The function to route 403 access forbidden template.

    Attributes:
        error (string): The particular error

    Returns:
        Redirection to the error template
    """
    return render_template('errors/403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    """
    The function to route 404 not found template.

    Attributes:
        error (string): The particular error

    Returns:
        Redirection to the error template
    """
    return render_template('errors/404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    """
    The function to route 500 internal error template.

    Attributes:
        error (string): The particular error

    Returns:
        Redirection to the error template
    """
    return render_template('errors/500.html'), 500
