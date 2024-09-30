import requests
from requests.auth import HTTPBasicAuth
import json

# Corrected API endpoint
url = "atlassian.net url comes here"

API_TOKEN = "API tocken comes here"

auth = HTTPBasicAuth("email_id_comes_here", API_TOKEN)

headers = {
    "Accept": "application/json"
}   

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

# Check the status code
print(f"Status Code: {response.status_code}")

# Print the response text to inspect
print(f"Response Text: {response.text}")

# Proceed if the response is successful
if response.status_code == 200:
    try:
        output = json.loads(response.text)
        print(f"JSON Output: {output}")

        # Safely access project name
        if output and isinstance(output, list) and "name" in output[0]:
            name = output[0]["name"]
            print(f"Project Name: {name}")
        else:
            print("Unexpected JSON structure or missing 'name' field.")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")