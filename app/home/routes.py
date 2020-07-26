from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.base.requests import *
import json


@blueprint.route('/index')
@login_required
def index():
    token = current_user.token
    gitlab_username = current_user.gitlab_username
    # closed = len(get_closed_issues(token))
    # issues_opened = get_open_issues(token)
    # opened = len(issues_opened)
    # in_progress = len(get_issues_in_progress(token))
    closed = 0
    issues_opened = 0
    opened = 0
    in_progress = 0
    total = closed + opened
    issues = get_all_issues(token)
    print(type(issues))
    return render_template('index.html',
                           issues_open_length=opened, issues_opened=issues_opened,
                           issues_in_progress=in_progress,
                           total_issues=total,
                           last_merge=get_latest_merge(token),
                           user_profile=get_user_profile(
                               gitlab_username, token),
                           issue_list=get_issues_in_progress(token))


@blueprint.route('/<template>')
def route_template(template):
    token = current_user.token
    gitlab_username = current_user.gitlab_username
    user_profile = get_user_profile(gitlab_username, token)
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html', user_profile=user_profile)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500
