import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ACCUWEATHER_API_KEY")

def get_current_weather(location_key):
    url = f"https://dataservice.accuweather.com/currentconditions/v1/{location_key}"
    params = { "apikey": API_KEY }
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("Error:", resp.status_code, resp.text)
        return
    data = resp.json()
    if not data:
        print("No weather data found.")
        return
    # Print basic details for now
    current = data[0]
    print("Weather:", current.get("WeatherText"))
    print("Temperature:", current['Temperature']['Imperial']['Value'], "F")
    print("Humidity:", current.get("RelativeHumidity"), "%")

if __name__ == "__main__":
    location_key = input("Enter location key: ")
    get_current_weather(location_key)