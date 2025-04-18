import requests
from datetime import datetime
import time

MY_LAT = 51.079263 # Your latitude
MY_LONG = 17.043416 # Your longitude

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return not (sunrise < time_now.hour < sunset)

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude

#Your position is within +5 or -5 degrees of the ISS position.
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    iss_lat, iss_long = get_iss_position()
    if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LONG - 5 < iss_long < MY_LONG + 5:
        #send mail
        pass
    time.sleep(1)




