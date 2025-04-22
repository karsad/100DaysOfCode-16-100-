import requests
from datetime import datetime
USERNAME = "karsad"
TOKEN = "hsd8y73r87sdfuyas87r3"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Learning Python Graph",
    "unit": "minute",
    "type": "int",
    "color": "kuro"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
print(pixel_endpoint)
today = datetime.today()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

today_pixel_config = {"quantity": "125"}
today_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime("%Y%m%d")}"
# response = requests.put(url=today_pixel_endpoint, json=today_pixel_config, headers=headers)
# response = requests.delete(url=today_pixel_endpoint, headers=headers)
print(response.text)