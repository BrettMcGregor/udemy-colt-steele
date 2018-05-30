import requests
url = "https://www.icanhazdadjoke.com"
response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()
print(data["joke"])
