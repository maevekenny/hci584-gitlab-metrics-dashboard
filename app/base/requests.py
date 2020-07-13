import requests
import gitlab
import mimetypes

GITLAB_TOKEN = 'pLey582NjxGWUAw5FccS'
GIT_URL = 'https://gitlab.com/api/v4/'
HEADERS = {
    'PRIVATE-TOKEN': GITLAB_TOKEN,
    'Cookie': '__cfduid=d4a124cd7752fdcaf227818d5168d6f931592882010; experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltSmpNbVV3WkdFM0xUWTVOalF0TkRjek15MWhPV0U1TFRRek9URXlNakJoTkRneU1pST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--5c41b5780ea26066e8c69050fa0e739eb239d7a3'
}
PAYLOAD = {}
GROUP_ID = '278964'


def get_gitlab_project(self):
    url = GIT_URL + "/projects"
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    print(response.text.encode('utf8'))


def get_closed_issues():
    url = GIT_URL + "/projects/" + GROUP_ID + "/issues?scope=all&state=closed"
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    return response.text.encode('utf8')


def get_issues_in_progress():
    url = GIT_URL + "/projects/" + GROUP_ID + \
        "/issues/?state=opened&labels=workflow::In dev"
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    return response.text.encode('utf8')


def get_open_issues():
    url = GIT_URL + "/projects/" + GROUP_ID + \
        "/issues/?state=opened&labels=workflow::ready for development"
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    return response.text.encode('utf8')


def get_milestones():
    url = GIT_URL + "/projects/" + GROUP_ID + "/milestones"
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    print(response.text.encode('utf8'))


def get_latest_merge():
    url = GIT_URL + "/projects/" + GROUP_ID + "/merge_requests/?state=merged"
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    return response.json()[0]

# # def get_issues_for_milestone(milestone_id, group_id)

# # # validates that the user credentials are valid for GitLab
# # def validate_credentials(username, token):
# #     # if username & token works against GitLab API:
# #     #     return True
# #     # else:
# #     #     # display an error for the user to reenter
# #     #     return False

# # # get the GitLab groups that the user has access to
# def get_groups():

#   url = "https://gitlab.us.lmco.com/api/v4/groups/compass/projects?include_subgroups=true&per_page=100"

#   payload = {}
#   headers= {}

#   response = requests.request("GET", url, headers=headers, data = payload)

#   print(response.text.encode('utf8'))
