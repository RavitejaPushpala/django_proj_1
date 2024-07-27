import requests

endpoint = "http://localhost:8000/api/products/12131312/"

response = requests.get(endpoint)
print(response.json())