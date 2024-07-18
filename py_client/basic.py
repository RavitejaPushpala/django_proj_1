import requests

endpoint = "http://localhost:8000/api"

response = requests.get(endpoint,json={"query":"hello world"})
print(response.text)