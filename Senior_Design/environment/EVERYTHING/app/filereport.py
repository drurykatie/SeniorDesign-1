import requests
import json

url = 'https://www.virustotal.com/vtapi/v2/url/report'

params = {'apikey': '989c64be41dd704e7e834beb72774fe3e4c837e15bd1807f2284eb563e62135b', 'resource':'<resourceinputbyuser>'}

response = requests.get(url, params=params)

print(json.dumps(response.json()))
