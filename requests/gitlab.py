import requests
import gitlab

GITLAB_TOKEN = 'pLey582NjxGWUAw5FccS'
GIT_URL = 'https://gitlab.com/gitlab-org/gitlab'



def get_gitlab_project(self):
    """Get numerical GitLab Project ID.

    Returns:
        int: Project ID number.

    Raises:
        foremast.exceptions.GitLabApiError: GitLab responded with bad status
            code.

    """
    self.server = gitlab.Gitlab(GIT_URL, private_token=GITLAB_TOKEN, api_version=4)
    project = self.server.projects.get(self.git_short)

    if not project:
        raise GitLabApiError('Could not get Project "{0}" from GitLab API.'.format(self.git_short))

    self.project = project
    return self.project 

print(get_gitlab_project)