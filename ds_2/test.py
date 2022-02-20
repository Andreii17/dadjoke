import requests
import json

query = {
    'page' : 1,
    'limit' : 20,
    'term' : 'coffe'
}
response = requests.get("https://icanhazdadjoke.com/search", params=query)
print(response)
print(response.content)

# content = response.content
# print(content)
# print(response.json()['response'])

# data = json.loads(response.text)
# print(data)