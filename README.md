# weather-project-app
Django Weather Project


import requests

def get_weather_data(city, api_key):
    """
    Fetches weather data from the OpenWeatherMap API.

    Args:
        city: The name of the city.
        api_key: Your OpenWeatherMap API key.

    Returns:
        A dictionary containing the weather data.
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return None

    return data

def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    city = "Malindi"  # Replace with the desired city

    weather_data = get_weather_data(city, api_key)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        icon = weather_data["weather"][0]["icon"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Icon: {icon}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    main()
