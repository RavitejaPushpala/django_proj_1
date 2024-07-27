import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"Hello world 3",
    "price": 13.99
}
response = requests.post(endpoint,json=data)
print(response.json())