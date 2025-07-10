import requests

api_key = "" # Create  API key in the website and paste here to access the weather-data.

own_endpoint ="https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": "17.688112",
    "lon": "83.213120",
    "appid":api_key,
    "cnt" :4
}

response = requests.get(url=own_endpoint,params=weather_params)

response.raise_for_status()

weather_data = response.json()

# weather_list = weather_data['list'][0]['weather'][0]['id']

'''
TO check the weather condition based on id.
To check if id (less than 700) return user to bring the Umbrella.
'''

will_rain = False

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")