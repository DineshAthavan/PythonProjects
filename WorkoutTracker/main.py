import requests
from datetime import datetime
import os
from dotenv import load_dotenv

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
APP_ENDPOINT = "https://app.100daysofpython.dev"
SHEETY_ENDPOINT = "https://api.sheety.co/3026986732da1209c12e50af29da44bd/workouts/workouts"

headers = {
    "x-app-id" :  APP_ID,
    "x-app-key" : API_KEY,
}

Workout_params = {
  "query": "Running for 10 minutes",
  "weight_kg": 64,
  "height_cm": 180,
  "age": 30,
  "gender": "male",
}

Workout_PostUrl = f"{APP_ENDPOINT}/v1/nutrition/natural/exercise"

response = requests.post(url=Workout_PostUrl, json=Workout_params, headers=headers)
print(response.status_code)
data = response.json()
print(data)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_data, auth=(os.getenv("SHEETY_USER"),os.getenv("SHEETY_PWD")))
    print(sheet_response.text)