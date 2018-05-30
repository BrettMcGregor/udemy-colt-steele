import requests
import random

while True:
    search = input("\nLet me tell you a joke! Give me a topic or Q to quit: ")

    if search.upper() == "Q":
        print("OK. See you next time.")
        break
    else:
        url = "https://www.icanhazdadjoke.com/search"

        response = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": search}
        )

        data = response.json()
        number_jokes = len(data["results"])

        if number_jokes == 0:
            print("Sorry. No jokes for that topic. Please try again.")
        else:
            print(f"I've got {number_jokes} jokes about {search}. Here's one:\n")
            print(random.choice(data["results"])["joke"])
