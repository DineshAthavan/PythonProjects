import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 9.919362
MY_LONG = 78.119314


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_cond = iss_latitude >= MY_LAT - 5.0 and iss_latitude <= MY_LAT + 5.0
    long_cond = iss_longitude >= MY_LONG - 5.0 and iss_longitude <= MY_LONG + 5.0

    if lat_cond and long_cond:
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_dark() and is_iss_overhead():

        user_name = "dineshathavantest1@gmail.com"
        password = "phyligjhdrsiugsl"

        with smtplib.SMTP("smtp.gmail.com", 578) as connection:
            connection.starttls()
            connection.login(user=user_name, password=password)
            connection.sendmail(from_addr=user_name,
                                to_addrs="dineshsmart1996@gmail.com",
                                msg="Subject:Look up\n\nISS at your location"
                                )

