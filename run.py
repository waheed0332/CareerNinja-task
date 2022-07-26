import requests
import json

url = "http://127.0.0.1:5000/check-similarity"

payload = json.dumps({
  "sentance1": "Investors unfazed by correction as crypto funds see $154 million inflows",
  "sentance2": "Bitcoin, Ethereum prices continue descent, but crypto funds see inflows"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
