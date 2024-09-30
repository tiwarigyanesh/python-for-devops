# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json

# creating flask app instance
app= Flask(__name__)

@app.route("/createJira", methods=['POST'])
def createJira():
    url = "atlassian.net url comes here"

    API_TOKEN = "API token comes here"

    auth = HTTPBasicAuth("email_id_comes_here", API_TOKEN)

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
    
    request_data = request.get_json()

    #print("Received request data:", request_data)
    comment_body = request_data.get('comment', {}).get('body', '')

    if '/jira' in comment_body:
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
    
#    request_data = request.get_json()

#    if "/jira" in request_data.get("body", ""):
      try:
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
      except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to create Jira ticket due to an exception."}), 500
    else:
      #print("No '/jira' found in body:", request_data.get("body", ""))
      return jsonify({"message": "Please provide '/jira' in the request body to create a Jira ticket."}), 400

# try this simple sample app to run on ec2 instance
app.run('0.0.0.0', port=5000)