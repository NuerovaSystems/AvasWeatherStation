# Ava's Weather Station

Ava's Weather Station is a full-stack project combining a Python Flask backend, AccuWeather API integration, and a stylish JavaScript-powered dashboard frontend.

Check real-time weather and multi-day forecasts for any city–all in your browser.

---

## Features

- **Live City & State Weather**: Get current conditions for any US city.
- **Multi-Day Forecasts**: 1, 5, 10, or 15-day options via AccuWeather.
- **Beautiful Dashboard**: Modern HTML, CSS, and JavaScript frontend.
- **Modular API**: Clean endpoints (`/weather/current`, `/weather/forecast`) to power web or mobile apps.
- **Secure**: API keys are kept private with `.env` and `.gitignore`.

---

## Quick Start

1. **Clone the repo**:
   ```
   git clone https://github.com/NuerovaSystems/AvasWeatherStation.git
   cd AvasWeatherStation
   ```

2. **Set up environment**
   - Install Python dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Add `.env` with your AccuWeather key:
     ```
     ACCUWEATHER_API_KEY=your_api_key_here
     ```

3. **Run the Flask server**:
   ```
   python app.py
   ```
   *(Use `python app.py --port=5001` if you need a different port.)*

4. **Open the dashboard**:  
   Visit `http://127.0.0.1:5000/index.html` (or your chosen port).

---

## API Endpoints

### `/weather/current`
- Params: `city`, `state`
- Returns: current weather as JSON

### `/weather/forecast`
- Params: `city`, `state`, `days` (`1`, `5`, `10`, or `15`)
- Returns: daily forecasts as JSON

---

## Security

- API key is stored in `.env` (never tracked by git thanks to `.gitignore`)
- Never share your `.env` or API keys

---

## Credits

Frontend & backend built by Ava Hughes.  
Weather powered by [AccuWeather](https://developer.accuweather.com/).

---

## License

General Public License
