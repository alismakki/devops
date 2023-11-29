#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import base64

personal_access_token = 'vigfbgqbb2jcikgs3bs7gdnxsqgnpmth4axa7wcb4kohtrrpx3hq'
encoded_pat = base64.b64encode(bytes(':' + personal_access_token, 'utf-8')).decode('ascii')

organization = 'DemandAutomation'
project = 'DTMO-Demand Automation'
feature_workitem_id = 17 

# API endpoint for creating a work item
url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/$User Story?api-version=6.0"

headers = {
    'Content-Type': 'application/json-patch+json',
    'Authorization': 'Basic ' + encoded_pat
}

# User Story titles
user_story_titles = [
    "SOW", "Solution Proposal", "MVP1", "MVP2", "MVP3", "MVP4", "MVP5",
    "MVP6", "MVP7", "MVP8", "MVP9", "Go-live", "Bid Package", "Contract Cycle and Awarding"
]

# Function to create a user story and link it to a feature
def create_user_story(title):
    json = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": title
        },
        {
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "System.LinkTypes.Hierarchy-Reverse",
                "url": f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/{feature_workitem_id}",
                "attributes": {
                    "comment": "Linking Usr Story to Feature"
                }
            }
        }
    ]
    response = requests.post(url, headers=headers, json=json)
    if response.status_code == 200:
        print(f"User Story '{title}' created and linked to feature successfully.")
    else:
        print(f"Failed to create User Story '{title}'. Status Code: {response.status_code}")
        print(response.text)  # This will print the entire response body

# Create user stories and link them to the feature
for title in user_story_titles:
    create_user_story(title)


# In[ ]:




