import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title":"Hello world modified",
    "price": 20.19
}
response = requests.put(endpoint,json=data)
print(response.json())