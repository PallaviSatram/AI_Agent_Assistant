from langchain import tool
import random
import requests

@tool
def tell_joke(category: str = "programming") -> str:
    """
    Fetch a random joke from the JokeAPI.
    Available categories: 'Programming', 'Misc', 'Pun', 'Spooky', 'Christmas'.
    """
    
    valid_categories = ["Programming", "Misc", "Pun", "Spooky", "Christmas"]
    if category not in valid_categories:
        category = "Programming"
    
    url = f"https://v2.jokeapi.dev/joke/{category}?safe-mode"

    try :
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("error"):
            return "Couldn't fetch a joke right now 😅 — please try again."

        # Handle single or two-part jokes
        if data["type"] == "single":
            return f"😂 {data['joke']}"
        else:
            return f"🤣 {data['setup']} — {data['delivery']}"

    except Exception as e:
        return f"⚠️ Error fetching joke: {e}"