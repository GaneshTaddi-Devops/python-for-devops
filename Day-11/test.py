import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

#print(complete_details[0]["id"],complete_details[0]["user"]["login"])

for users in range(len(complete_details)):
    print(complete_details[users]["user"]["login"])
