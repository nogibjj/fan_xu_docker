import requests

url = "https://zenquotes.io/api/random"


response = requests.get(url)

print(response.text)
