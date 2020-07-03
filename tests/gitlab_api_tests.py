#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import urllib3
from urllib.error import HTTPError

# Get all the projects in the Compass group - lists their latest tag & the latest successful tagged pipeline
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

compass_subgroups_url = "https://gitlab.us.lmco.com/api/v4/groups/compass/projects/?include_subgroups=true&per_page=100"

# Insert either your individual private token or compass-bot (never check it in)
headers= {"PRIVATE-TOKEN": "<PRIVATE TOKEN>"}
proxies={"http_proxy":"http://proxy-lmi.global.lmco.com:80", "https_proxy":"http://proxy-lmi.global.lmco.com:80"}

# Get all the projects under the Compass group
compass_projects = requests.request("GET", compass_subgroups_url, headers=headers, data = {}, proxies=proxies, verify=False)
pretty_json = json.loads(compass_projects.text.encode('utf8'))
tag_dict = {}
for project in pretty_json:
        project_id = project['id']
        project_name = project['name']
        project_tag_request = "https://gitlab.us.lmco.com/api/v4/projects/" + str(project_id) + "/repository/tags"
        pipeline_request = "https://gitlab.us.lmco.com/api/v4/projects/" + str(project_id) + "/pipelines"
        latest_project_tag = requests.request("GET", project_tag_request, headers=headers, data = {}, proxies=proxies, verify=False)
        project_tag_json = json.loads(latest_project_tag.text.encode('utf8'))
        if len(project_tag_json) > 0 and type(project_tag_json) is list:
            pipeline_request = "https://gitlab.us.lmco.com/api/v4/projects/" + str(project_id) + "/pipelines?status=success&scope=tags"
            last_pipeline = requests.request("GET", pipeline_request, headers=headers, data = {}, proxies=proxies, verify=False)
            pipeline_json = json.loads(last_pipeline.text.encode('utf8'))
            if len(pipeline_json) > 0:
                latest_tag = project_tag_json[0].get("name", None)
                latest_successful_pipeline_tag = pipeline_json[0].get("ref", None)
                tag_dict[project_name]=latest_tag
                if(latest_tag is latest_successful_pipeline_tag):
                    print('\x1b[31m' + project_name + '\x1b[0m' + ': SUCCESS')
                else:
                    print('\x1b[31m' + project_name + '\x1b[0m' + ': The latest tag is: ' + latest_tag + ' -- the latest successful tagged pipeline is: ' + latest_successful_pipeline_tag)


# In[ ]:


print(project)


# In[ ]:


print('\x1b[50m' + project_name + '\x1b[0m')


# In[ ]:


import requests
import json
import urllib3
from urllib.error import HTTPError

# Gets the list of the UUIDs of all the projects in the Compass group
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

compass_subgroups_url = "https://gitlab.us.lmco.com/api/v4/groups/compass/projects/?include_subgroups=true&per_page=100"

# Insert either your individual private token or compass-bot (never check it in)
headers= {"PRIVATE-TOKEN": ""}
proxies={"http_proxy":"http://proxy-lmi.global.lmco.com:80", "https_proxy":"http://proxy-lmi.global.lmco.com:80"}

compass_projects = requests.request("GET", compass_subgroups_url, headers=headers, data = {}, proxies=proxies, verify=False)
pretty_json = json.loads(compass_projects.text.encode('utf8'))
tag_dict = {}
for project in pretty_json:
        project_id = project['id']
        project_name = project['name']
        print(project_name + ' - ' + str(project_id))


# In[4]:


import requests
import json
import urllib3
from urllib.error import HTTPError

# Gets a list of all the projects in the Compass group & lists some information about them. Used this to create an excel file for Joe.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

compass_subgroups_url = "https://gitlab.us.lmco.com/api/v4/groups/compass/projects/?include_subgroups=true&per_page=100"

# Insert either your individual private token or compass-bot (never check it in)
headers= {"PRIVATE-TOKEN": "<PRIVATE TOKEN>"}
proxies={"http_proxy":"http://proxy-lmi.global.lmco.com:80", "https_proxy":"http://proxy-lmi.global.lmco.com:80"}

compass_projects = requests.request("GET", compass_subgroups_url, headers=headers, data = {}, proxies=proxies, verify=False)
pretty_json = json.loads(compass_projects.text.encode('utf8'))
tag_dict = {}
for project in pretty_json:
        project_id = project['id']
        project_name = project['name']
        project_link = project['web_url']
        project_build_svg = project_link + '/badges/master/pipeline.svg'
        project_description = project['description']
        tag_dict[project_name]=[project_link, project_id]
        print('"name": "' + project_name + '",')
#         print('"description": "'+ project_description + '",')

        print('"statuslink": "'+ project_link + '",')
        print('"src": "'+ project_build_svg  + '",')
        print('"id": "' + str(project_id) + '",')
        print('')





