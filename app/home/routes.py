from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.base.requests import get_closed_issues, get_issues_in_progress, get_open_issues, get_latest_merge


@blueprint.route('/index')
@login_required
def index():
    # closed = len(get_closed_issues())
    # issues_opened = get_open_issues()
    # opened = len(issues_opened)
    # in_progress = len(get_issues_in_progress())
    closed = 0
    issues_opened = 0
    opened = 0
    in_progress = 0
    total = closed + opened
    print('test')

    return render_template('index.html',
                           issues_open_length=opened, issues_opened=issues_opened,
                           issues_in_progress=in_progress,
                           total_issues=total,
                           last_merge=get_latest_merge())


@blueprint.route('/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500
