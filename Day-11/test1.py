import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

user_present_count = {}

#print(complete_details[0]["id"],complete_details[0]["user"]["login"])

for users in range(len(complete_details)):
    print(complete_details[users]["user"]["login"])

    username = complete_details[users]["user"]["login"]

    if username in user_present_count:
        user_present_count[username] += 1
    else:
        user_present_count[username] = 1

print()
print (user_present_count)
