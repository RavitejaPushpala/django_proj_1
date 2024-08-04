import requests

headers = {'Authorization': 'bearer 5d0ad2970d4d2d4b2c4ddd661550f4aa8d9b1398'}

endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"Hello world 3",
    "price": 13.99
}
response = requests.post(endpoint,json=data,headers=headers)
print(response.json())