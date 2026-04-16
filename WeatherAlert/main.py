import requests
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get(OWM_API_KEY)
lat = 11.016844
lon = 76.955833

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
}

response = requests.get(OWM_ENDPOINT, params=params)
print(response.status_code)
