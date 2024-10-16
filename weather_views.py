import requests
from django.shortcuts import render

def index(request):
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    city = "Malindi"  # Replace with the desired city

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return render(request, "weather_error.html", {"error_message": "Unable to fetch weather data."})

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    context = {
        "temperature": temperature,
        "description": description,
        "icon": icon,
        "humidity": humidity,
        "wind_speed": wind_speed
    }

    return render(request, "weather.html", context)
