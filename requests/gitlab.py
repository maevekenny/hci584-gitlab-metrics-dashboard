import requests
import gitlab
import http.client
import mimetypes

GITLAB_TOKEN = 'pLey582NjxGWUAw5FccS'
GIT_URL = 'https://gitlab.com/gitlab-org/gitlab'

conn = http.client.HTTPSConnection("gitlab.com")
payload = ''
headers = {
  'Cookie': '__cfduid=d4a124cd7752fdcaf227818d5168d6f931592882010; experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltSmpNbVV3WkdFM0xUWTVOalF0TkRjek15MWhPV0U1TFRRek9URXlNakJoTkRneU1pST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--5c41b5780ea26066e8c69050fa0e739eb239d7a3; _gitlab_session=902cd5acb4f5b1ab80785fa407587703'
}
conn.request("GET", "/api/v4/projects/278964?PRIVATE-TOKEN=pLey582NjxGWUAw5FccS", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# def get_gitlab_project(self):
    # """Get numerical GitLab Project ID.

    # Returns:
    #     int: Project ID number.

    # Raises:
    #     foremast.exceptions.GitLabApiError: GitLab responded with bad status
    #         code.

    # """
    # self.server = gitlab.Gitlab(GIT_URL, private_token=GITLAB_TOKEN, api_version=4)
    # project = self.server.projects.get(self.git_short)

    # if not project:
    #     raise GitLabApiError('Could not get Project "{0}" from GitLab API.'.format(self.git_short))

    # self.project = project
    # return self.project 

# def get_all_issues(group_id):

# def get_milestones(group_id):

# def get_issues_for_milestone(milestone_id, group_id)

# # validates that the user credentials are valid for GitLab
# def validate_credentials(username, token):  
#     # if username & token works against GitLab API:
#     #     return True
#     # else:
#     #     # display an error for the user to reenter
#     #     return False

# # get the GitLab groups that the user has access to
# def get_groups(): 
#    	Hit the GitLab API to get the list of groups that the user has access to
# Return group



# print(get_gitlab_project)