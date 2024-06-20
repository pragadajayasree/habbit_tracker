import requests
from datetime import datetime

pixela_end_point = "https://pixe.la/v1/users"
TOKEN = "abcdefghij"
USERNAME = "jayasree"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response1 = requests.post(url=pixela_end_point,json=pixela_parameters)
# print(response1.text)

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"
ID = "graph1"
graph_parameters = {
    "id": ID,
    "name": "course tracker",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response2 = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response2.text)
current_day = datetime(year=2024, month=6, day=19)
pixel_endpoint = f"{graph_endpoint}/{ID}"
pixel_parameters = {
    "date": current_day.strftime("%Y%m%d"),
    "quantity": "10"
}

# response3 = requests.post(url=pixel_endpoint, headers=headers, json=pixel_parameters)
# print(response3.text)

update_endpoint = f"{pixel_endpoint}/20240619"
update_parameters = {
    "quantity": "30"
}
# response4 = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
# print(response4.text)
delete_endpoint = f"{pixel_endpoint}/20240619"
response5 = requests.delete(url=delete_endpoint, headers=headers)
print(response5.text)
