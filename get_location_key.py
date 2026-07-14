import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ACCUWEATHER_API_KEY")

def get_location_key(city, state):
    url = "https://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": API_KEY,
        "q": f"{city}, {state}",
    }
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("Error:", resp.status_code, resp.text)
        return None
    data = resp.json()
    if not data:
        print("No location found.")
        return None
    # Grab the first match
    key = data[0].get("Key")
    name = data[0].get("LocalizedName")
    area = data[0].get("AdministrativeArea", {}).get("ID")
    print(f"Location key for {name}, {area}: {key}")
    return key

if __name__ == "__main__":
    city = input("City: ")
    state = input("State (2-letter, e.g. TX): ")
    get_location_key(city, state)