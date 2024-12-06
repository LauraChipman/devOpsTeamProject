from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API Key for OpenWeatherMap
API_KEY = "8117ef82349de9509894acdad6bb6261"

@app.route("/")
def home():
    return render_template("index.html")  # Serve the HTML page

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.json.get("city")  # Get city name from the request
    if not city:
        return jsonify({"error": "City not provided"}), 400

    # Fetch weather data from OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    weather_info = {
        "name": data["name"],
        "icon": data["weather"][0]["icon"],
        "description": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }
    return jsonify(weather_info)  # Return the weather data as JSON

if __name__ == "__main__":
    app.run(debug=True)
