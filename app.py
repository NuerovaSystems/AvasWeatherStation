import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ACCUWEATHER_API_KEY")

app = Flask(__name__, static_folder='.', static_url_path='')

def get_location_key(city, state):
    url = "https://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": API_KEY,
        "q": f"{city}, {state}",
    }
    resp = requests.get(url, params=params)
    if resp.status_code != 200 or not resp.json():
        return None
    data = resp.json()
    return data[0]["Key"]

def get_current_weather(location_key):
    url = f"https://dataservice.accuweather.com/currentconditions/v1/{location_key}"
    params = { "apikey": API_KEY }
    resp = requests.get(url, params=params)
    if resp.status_code != 200 or not resp.json():
        return None
    return resp.json()[0]

@app.route('/weather/current')
def current_weather():
    city = request.args.get("city")
    state = request.args.get("state")
    if not city or not state:
        return jsonify({"error": "city and state are required"}), 400
    location_key = get_location_key(city, state)
    if not location_key:
        return jsonify({"error": "Could not find that location"}), 404
    weather = get_current_weather(location_key)
    if not weather:
        return jsonify({"error": "No weather data found"}), 502
    response = {
        "city": city.title(),
        "state": state.upper(),
        "condition": weather.get("WeatherText"),
        "temperature": weather['Temperature']['Imperial']['Value'],
        "units": "F",
        "humidity": weather.get("RelativeHumidity"),
        "timestamp": weather.get("LocalObservationDateTime")
    }
    return jsonify(response)

def get_forecast(location_key, days=5):
    url = f"https://dataservice.accuweather.com/forecasts/v1/daily/{days}day/{location_key}"
    params = { "apikey": API_KEY }
    resp = requests.get(url, params=params)
    if resp.status_code != 200 or not resp.json():
        return None
    return resp.json().get("DailyForecasts", [])

@app.route('/weather/forecast')
def weather_forecast():
    city = request.args.get("city")
    state = request.args.get("state")
    days = int(request.args.get("days", 5))  # default to 5 days if not given
    if days not in [1, 5, 10, 15]:
        return jsonify({"error": "days must be 1, 5, 10, or 15"}), 400
    if not city or not state:
        return jsonify({"error": "city and state are required"}), 400
    location_key = get_location_key(city, state)
    if not location_key:
        return jsonify({"error": "Could not find that location"}), 404
    forecast_data = get_forecast(location_key, days)
    if not forecast_data:
        return jsonify({"error": "No forecast data found"}), 502
    # Build a list of daily weather summaries
    forecast = []
    for day in forecast_data:
        forecast.append({
            "date": day.get("Date"),
            "condition": day["Day"].get("IconPhrase"),
            "min_temp": day["Temperature"]["Minimum"]["Value"],
            "max_temp": day["Temperature"]["Maximum"]["Value"],
            "units": day["Temperature"]["Minimum"]["Unit"]
        })
    response = {
        "city": city.title(),
        "state": state.upper(),
        "forecast": forecast
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5002)