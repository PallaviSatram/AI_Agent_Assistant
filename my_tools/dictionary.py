from langchain import tool
import requests
@tool
def word_meaning(word):
    """
    Fetches and prints the meaning of a given English word.
    Uses the Free Dictionary API (no key required).
    """
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(f"word '{word}' not found.")
            return
        meanings = data[0]["meanings"]
        print(f"\n Meaning(s) of '{word}: ")
        for meaning in meanings:
            part_of_speech = meaning["partOfSpeech"]
            definition = meaning["definitions"][0]["definition"]
            print(f" - ({part_of_speech}) {definition}")
    except Exception as e:
        print("Error fetching meaning: ",e)
