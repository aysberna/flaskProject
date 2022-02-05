import requests
import json
apiurl = "http://127.0.0.1:5000/api/users"
todo = {"username":"jamiryo","password":"123"}
headers = {"Content-Type":"application/json"}
response = requests.get(apiurl,headers=headers)
print(response.json())
print(response.status_code)

