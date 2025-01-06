import requests
def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        print("Here's a random joke:\n")
        print(f"Setup: {joke_data['setup']}")
        print(f"Punchline: {joke_data['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

if __name__ == "__main__":
        fetch_joke()