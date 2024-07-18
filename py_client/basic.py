import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint,params={"abc":123},json={"query":"hello world"})
print(response.json())