import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "97907",
    'client_secret': '11b7e72f80d8e6521742346523a26530901e84ac',
    'refresh_token': '3478a5154f912cfc26fab87962d5f50c9705a8f0',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
api_data = requests.get(activites_url, headers=header, params=param).json()

api_data = json.dumps(api_data)
client_id = payload['client_id']

title = 'api_data' + client_id + '.txt'
with open(title, 'ab') as file:
    for item in api_data:
        file.write(item.encode())
