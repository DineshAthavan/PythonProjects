import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get(OWM_API_KEY)
account_sid = os.environ.get(TWILIO_SID)
auth_token = os.environ.get(TWILIO_AUTH_TOKEN)
lat = 11.016844
lon = 76.955833

params = {
    "lat": lat,
    "lon": lon,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWM_ENDPOINT, params=params)
response.raise_for_status() #exception handling
weather_data = response.json()

x1 = weather_data["list"][0]["weather"][0]["main"]
x2 = weather_data["list"][0]["weather"][0]["description"]
msg_content = f"{x1}\n{x2}"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=msg_content,
    from_=os.environ.get(FROM_NUMBER),
    to="<entermyphno>",
)
