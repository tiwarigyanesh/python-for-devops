from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
#create flask app instance
app= Flask(__name__)

@app.route("/createJIRA", method["POST"])
    
def createJIRA():

        # This code sample uses the 'requests' library:
    # http://docs.python-requests.org


    url = "atlassian.net url comes here"

    API_TOKEN = "API token comes here"

    auth = HTTPBasicAuth("emailid_comes_here", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "KAN"
        },
        "issuetype": {
        "id": "10005"
        },
        "summary": "First Jira Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))