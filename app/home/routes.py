from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.base.requests import *
import json

"""
HCI 584 - Summer 2020
The module that holds the  blueprint route template configurations.

Author: Maeve Kenny
"""
@blueprint.route('/index')
@login_required
def index():
    """
    The index route template

    Returns:
        Redirection to index.html
    """
    token = current_user.token
    issue_stats = get_issue_statistics(token)
    in_progress_stats = get_in_progress_issue_statistics(token)
    gitlab_username = current_user.gitlab_username
    return render_template('index.html',
                           issues_open_count=issue_stats['statistics']['counts']['opened'],
                           issue_in_progress_count=in_progress_stats['statistics']['counts']['opened'],
                           issues_total_count=issue_stats['statistics']['counts']['all'],
                           last_merge=get_latest_merge(token),
                           user_profile=get_user_profile(
                               gitlab_username, token),
                           issue_list=get_issues_in_progress(token),
                           weekly_issues=get_issue_stats_by_week(token),
                           monthly_issues=get_issue_stats_by_month(token))


@blueprint.route('/<template>')
def route_template(template):
    """
    The blueprint route template.

    Attributes:
        template (string): The template page

    Returns:
        Redirection to the particular template passed in
    """
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
