import requests
from twilio.rest import Client
import os

ACC_SID = "ACd8ee0095c7826d86499d7b625b161d"

MY_LATITUDE = 6.461250
MY_LONGITUDE = -71.734261

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("API_KEY")
API_CONFIG = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY
}

def check_if_it_rains(data: dict) -> bool:
    for weather in data['list']:
        if weather['weather'][0]['id'] < 700:
            return True
    return False

request = requests.get(API_URL, API_CONFIG)
print(f"Requests http code: {request.status_code}")
request.raise_for_status()
data = request.json()

print(data)
print(data["list"][0]["weather"])
print(os.environ.get("ACC_TOKEN"))

if check_if_it_rains(data):
    client = Client(ACC_SID, os.environ.get("ACC_TOKEN"))
    message = client.messages.create(
        body="Wez parasolkę! ☔️",to=os.environ.get("MY_PHONE"),from_="+19787055741"
    )
    print(message.sid)