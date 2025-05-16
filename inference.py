import requests
import json

data = json.dumps({"features": [1, 2, 3]})
headers = {"Content-Type": "application/json"}

response = requests.post("http://localhost:5000/predict", data=data, headers=headers)
print(response.json())
