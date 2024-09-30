import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

pull_details = response.json()

# print(pull_details[1]["id"])

# print(pull_details[0]["user"]["login"])

# to get all user, having pull request

for i in range(len(pull_details)):
  print(pull_details[i]["user"]["login"])