import requests

responce = requests.get('127.0.0.1:8000/recipe')

print(responce)