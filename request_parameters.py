import requests
url = "https://www.icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "dog"}
)

data = response.json()
for result in data["results"]:
    print(result["joke"], end="\n\n" + "*" * 90 + "\n\n")

