import requests

api_key = "" # Create  API key in the website and paste here to access the weather-data.

own_endpoint ="https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": "17.688112",
    "lon": "83.213120",
    "appid":api_key,
}

response = requests.get(url=own_endpoint,params=weather_params)

response.raise_for_status()

weather_data = response.json()

print(weather_data)