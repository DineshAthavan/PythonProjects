import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
SHEETY_GET_ENDPOINT = "https://api.sheety.co/3026986732da1209c12e50af29da44bd/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.pwd = os.getenv("SHEETY_PWD")
        self.to_data = {}


    def get_to_data(self):
        response = requests.get(url=SHEETY_GET_ENDPOINT,auth=(self.username,self.pwd))
        data = response.json()
        self.to_data = data['prices']
        return self.to_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_GET_ENDPOINT}/{row_id}",
            json=new_data,
            auth=(self.username,self.pwd)
        )