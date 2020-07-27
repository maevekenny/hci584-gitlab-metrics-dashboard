import requests
import gitlab
import mimetypes
from datetime import datetime, timedelta
from flask_login import login_required, current_user

# GitLab URL - can change for another GitLab server
GIT_URL = 'https://gitlab.com/api/v4/'
PROJECT_ID = '278964'


def get_gitlab_projects(token):
    """
    Request to get projects that the user has access to.

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of projects

    """
    url = GIT_URL + "projects"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_issues(token):
    """
    Request to get all issues for a particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + "/issues?per_page=10"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_issue_statistics(token):
    """
    Request to get issue statistics for all issues for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issue stats

    """
    url = GIT_URL + "projects/" + PROJECT_ID + "/issues_statistics?scope=all"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_in_progress_issue_statistics(token):
    """
    Request to get issue statistics for in progress issues for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issue stats

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=opened&labels=workflow::In dev"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_closed_issues(token):
    """
    Request to get closed issues for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + "/issues?scope=all&state=closed"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_january(token):
    """
    Request to get closed issues for January 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-01-01T00:00:01.00Z&updated_before=2020-01-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_february(token):
    """
    Request to get closed issues for February 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-02-01T00:00:01.00Z&updated_before=2020-02-28T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_march(token):
    """
    Request to get closed issues for March 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-02-01T00:00:01.00Z&updated_before=2020-02-28T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_april(token):
    """
    Request to get closed issues for April 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-04-01T00:00:01.00Z&updated_before=2020-04-30T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_may(token):
    """
    Request to get closed issues for May 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-05-01T00:00:01.00Z&updated_before=2020-05-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_june(token):
    """
    Request to get closed issues for June 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-06-01T00:00:01.00Z&updated_before=2020-06-30T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_july(token):
    """
    Request to get closed issues for July 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-07-01T00:00:01.00Z&updated_before=2020-07-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_all_closed_issues_in_august(token):
    """
    Request to get closed issues for August 2020 for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of closed issues

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues_statistics?state=closed&updated_after=2020-08-01T00:00:01.00Z&updated_before=2020-08-31T23:59:59.00Z"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_issue_stats_by_month(token):
    """
    Request to get issue statistics by month for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issue stats

    """
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
    """
    Request to get issue statistics by week from the current day for the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issue stats

    """
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
    """
    Request to get issues in progress from a particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issues in progress

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues/?state=opened&labels=workflow::In dev&per_page=10"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_open_issues(token):
    """
    Request to get open issues from a particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of issues in opened state

    """
    url = GIT_URL + "projects/" + PROJECT_ID + \
        "/issues/?state=opened&labels=workflow::ready for development"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_milestones(token):
    """
    Request to get milestones that are linked to a particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON array of milestones

    """
    url = GIT_URL + "projects/" + PROJECT_ID + "/milestones"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    print(response.text.encode('utf8'))


def get_latest_merge(token):
    """
    Request to get latest merged merge request to the particular project

    Parameters:
    token (string): GitLab API token of the user

    Returns:
    response: JSON object with merge request details

    """
    url = GIT_URL + "projects/" + PROJECT_ID + "/merge_requests/?state=merged"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()[0]


def get_user_profile(username, token):
    """
    Request to get user profile details for a particular username

    Parameters:
    username (string): GitLab username
    token (string): GitLab API token of the user

    Returns:
    response: JSON object with GitLab user profile

    """
    url = GIT_URL + "users?username=" + username
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()[0]
