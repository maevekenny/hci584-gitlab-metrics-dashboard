import requests
import gitlab
import mimetypes
from flask_login import login_required, current_user

GIT_URL = 'https://gitlab.com/api/v4/'
GROUP_ID = '278964'


def get_gitlab_project(token):
    url = GIT_URL + "/projects"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    print(response.text.encode('utf8'))


def get_all_issues(token):
    url = GIT_URL + "/projects/" + GROUP_ID + "/issues"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_closed_issues(token):
    print('user', current_user.token)

    url = GIT_URL + "/projects/" + GROUP_ID + "/issues?scope=all&state=closed"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.text.encode('utf8')


def get_issues_in_progress(token):
    url = GIT_URL + "/projects/" + GROUP_ID + \
        "/issues/?state=opened&labels=workflow::In dev"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_open_issues(token):
    url = GIT_URL + "/projects/" + GROUP_ID + \
        "/issues/?state=opened&labels=workflow::ready for development"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()


def get_milestones(token):
    url = GIT_URL + "/projects/" + GROUP_ID + "/milestones"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    print(response.text.encode('utf8'))


def get_latest_merge(token):
    url = GIT_URL + "/projects/" + GROUP_ID + "/merge_requests/?state=merged"
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()[0]


def get_user_profile(username, token):
    url = GIT_URL + "users?username=" + username
    response = requests.request(
        "GET", url, headers={'PRIVATE-TOKEN': token}, data={})
    return response.json()[0]

# # def get_issues_for_milestone(milestone_id, group_id)

# # # validates that the user credentials are valid for GitLab
# # def validate_credentials(username, token):
# #     # if username & token works against GitLab API:
# #     #     return True
# #     # else:
# #     #     # display an error for the user to reenter
# #     #     return False
