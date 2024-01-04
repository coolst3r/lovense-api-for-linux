import requests
import json

# Function request example
def send_function_request():
    url = "https://api.lovense-api.com/api/lan/v2/command"
    headers = {"Content-Type": "application/json"}
    payload = {
        "token": "YourDeveloperToken",
        "uid": "1132fsdfsd",
        "command": "Function",
        "action": "Vibrate:16",
        "timeSec": 20,
        "loopRunningSec": 9,
        "loopPauseSec": 4,
        "apiVer": 1
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.json())

# Pattern request example
def send_pattern_request():
    url = "https://api.lovense-api.com/api/lan/v2/command"
    headers = {"Content-Type": "application/json"}
    payload = {
        "token": "YourDeveloperToken",
        "uid": "1ads22adsf",
        "command": "Pattern",
        "rule": "V:1;F:v;S:1000#",
        "strength": "20;20;5;20;10",
        "timeSec": 9,
        "apiVer": 2
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.json())

# Preset request example
def send_preset_request():
    url = "https://api.lovense-api.com/api/lan/v2/command"
    headers = {"Content-Type": "application/json"}
    payload = {
        "token": "YourDeveloperToken",
        "uid": "1adsf2323",
        "command": "Preset",
        "name": "pulse",
        "timeSec": 9,
        "apiVer": 1
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.json())

# Make the requests
send_function_request()
send_pattern_request()
send_preset_request()
