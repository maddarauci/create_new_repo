import requests
import json 

print("Welcome bitch\t How may i help you...\noOOh you want to create a new repo")

user_name = input("enter your github name: ")
print(user_name)


github_token = input("enter your github token: ")
print(github_token)

repo_name = input("enter your repo name: ")
print(repo_name)

repo_desc = input("enter your repo description: ")
print(repo_desc)


payload = {'name': repo_name, 'description': repo_desc, 'auto_init': 'true'}
repo_request = requests.post('https://api.github.com/' + 'user/repos', auth=(user_name,github_token), data=json.dumps(payload))
if repo_request.status_code == 422:
    print("repo already exists, try with another name")
elif repo_request.status_code == 201:
    print("your repo is created")
elif repo_request.status_code == 401:
    print("your unauthorized user for this action.")