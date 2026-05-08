import requests
from datetime import datetime

Pixela_Endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "tfvoegdcksoagafefasgo4c0advd9",
    "username": "dineshathavan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=Pixela_Endpoint, json=user_params)
# print(response.text)

#Creating a new graph
# Graph_Endpoint = f"{Pixela_Endpoint}/dineshathavan/graphs"
# response = requests.post(url=Graph_Endpoint, json=user_params)
#
# graph_params = {
#     "id": "graph1",
#     "name": "Habit Tracker",
#     "unit": "Hours",
#     "type": "float",
#     "color": "ichou",
# }
#
headers = {
    "X-USER-TOKEN": "tfvoegdcksoagafefasgo4c0advd9"
}
#
# graph_response = requests.post(url=Graph_Endpoint, json=graph_params, headers=headers)
# print(graph_response.text)
#
PixelAdd_Endpoint = f"{Pixela_Endpoint}/dineshathavan/graphs/graph1"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.0",
}

pixel_response = requests.post(url=PixelAdd_Endpoint, json=pixel_params, headers=headers)
print(pixel_response.text)
#
# #Correction in previous data
# correction_date = "20260504"
# correction_endpoint = f"{Pixela_Endpoint}/dineshathavan/graphs/graph1/{correction_date}"
# correction_params = {
#     "quantity": "1.0"
# }
# correction_response = requests.put(url=correction_endpoint, json=correction_params,headers=headers)
# print(correction_response.text)
#
#
# #Deleting a pixel
# delete_response = requests.delete(url=correction_endpoint, headers=headers)
# print(delete_response.text)