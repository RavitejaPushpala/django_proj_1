import requests

headers = {'Authorization': 'bearer e56a3c494e5a07ac902eb4662f50151966141dbf'}

endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"Hello world 3",
    "price": 13.99
}
response = requests.post(endpoint,json=data,headers=headers)
print(response.json())