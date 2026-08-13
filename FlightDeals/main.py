import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from pprint import pprint
from notification_manager import NotificationManager


requests_cache.install_cache(cache_name="flight_cache",
                             urls_expire_after={
                                 '*': 3600,
                                 '*.sheety.co': 0,
                             }
                             )

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
print(tomorrow)
print(six_month_from_today)

data_manager = DataManager()
sheet_data = data_manager.get_to_data()
print(sheet_data)

notification_manager = NotificationManager()

for destination in sheet_data:
    flight_search = FlightSearch()
    flight_options = flight_search.check_flights(origin_city_code="LHR",
                                             destination_city_code=destination["iataCode"],
                                             from_time=tomorrow,
                                             to_time=six_month_from_today)

    cheapest_flight = find_cheapest_flight(flight_options, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        notification_manager.send_sms(
            message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )