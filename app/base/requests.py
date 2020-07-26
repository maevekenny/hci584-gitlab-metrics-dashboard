import requests
import gitlab
import mimetypes
from datetime import datetime, timedelta

from flask_login import login_required, current_user

# GitLab URL - can change for another GitLab server
GIT_URL = 'https://gitlab.com/api/v4/'
PROJECT_ID = '278964'


def get_gitlab_project(token):
    url = GIT_URL + "projects"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    print(response.text.encode('utf8'))


def get_all_issues(token):
    url = GIT_URL + "projects/" + PROJECT_ID + "/issues?per_page=10"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_issue_statistics(token):
    url = GIT_URL + "projects/" + PROJECT_ID + "/issues_statistics?scope=all"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_in_progress_issue_statistics(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=opened&labels=workflow::In dev"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_closed_issues(token):
    url = GIT_URL + "projects/" + PROJECT_ID + "/issues?scope=all&state=closed"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_january(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-01-01T00:00:01.00Z&updated_before=2020-01-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_february(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-02-01T00:00:01.00Z&updated_before=2020-02-28T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_march(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-02-01T00:00:01.00Z&updated_before=2020-02-28T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_april(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-04-01T00:00:01.00Z&updated_before=2020-04-30T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_may(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-05-01T00:00:01.00Z&updated_before=2020-05-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_june(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-06-01T00:00:01.00Z&updated_before=2020-06-30T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_july(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-07-01T00:00:01.00Z&updated_before=2020-07-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_august(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-08-01T00:00:01.00Z&updated_before=2020-08-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_issue_stats_by_month(token):

    # TODO: Don't hardcode the months - possibly use a better python library for date
    months = ["January", "February", "March",
              "April", "May", "June", "July"]
    counts_opened = []
    counts_closed = []

    for month in months:
        month_numeric = months.index(month) + 1
        end_of_month_index = 31

        # Adjust the end of the month date depending on the month
        if (month_numeric == 2):
            end_of_month_index = 28
        elif (month_numeric == 4) | (month_numeric == 6):
            end_of_month_index = 30

        url = GIT_URL + "projects/" + PROJECT_ID + \
            "/issues_statistics?updated_after=2020-0" + str(month_numeric) + "-01" + \
            "T00:00:01.00Z&updated_before=2020-0" + str(month_numeric) + \
            "-" + str(end_of_month_index) + "T23:59:59.00Z"

        response = requests.request(
            "GET", url, headers={'PRIVATE-TOKEN': token}, data={})

        counts_opened.append(response.json(
        )['statistics']['counts']['closed'])
        counts_closed.append(response.json(
        )['statistics']['counts']['opened'])

    return months, counts_opened, counts_closed


def get_issue_stats_by_week(token):
    # datetime object containing current date and time
    now = datetime.today()
    week_ago = now - timedelta(days=7)

    dates = []
    counts_opened = []
    counts_closed = []
    for x in range(8):
        date = week_ago + timedelta(days=x)
        formatted_date = date.strftime("%Y-%m-%d")

        url = GIT_URL + "projects/" + PROJECT_ID + \
            "/issues_statistics?updated_after=" + formatted_date + \
            "T00:00:01.00Z&updated_before=" + formatted_date + "T23:59:59.00Z"
        response = requests.request(
            "GET", url, headers={'PRIVATE-TOKEN': token}, data={})

        dates.append(formatted_date)
        counts_opened.append(response.json(
        )['statistics']['counts']['closed'])
        counts_closed.append(response.json(
        )['statistics']['counts']['opened'])
    return dates, counts_opened, counts_closed


def get_issues_in_progress(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues/?state=opened&labels=workflow::In dev"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_open_issues(token):
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues/?state=opened&labels=workflow::ready for development"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_milestones(token):
    url = GIT_URL + "projects/" + PROJECT_ID + "/milestones"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    print(response.text.encode('utf8'))


def get_latest_merge(token):
    url = GIT_URL + "projects/" + PROJECT_ID + "/merge_requests/?state=merged"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()[0]


def get_user_profile(username, token):
    url = GIT_URL + "users?username=" + username
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()[0]
