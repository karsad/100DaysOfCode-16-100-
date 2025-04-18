import requests
from datetime import datetime

# my_url = "http://api.open-notify.org/iss-now.json"
# response = requests.get(my_url)
# response.raise_for_status()
#
# data = response.json()
#
# print(response)
# print(data)
# print(data['iss_position']['longitude'])

my_url2 = "https://api.sunrise-sunset.org/json"
params = {
    "lat": 51.107883,
    "lng": 17.038538,
    "formatted": 0
}
response = requests.get(my_url2, params=params)
data = response.json()
print(data)
sunset = data['results']['sunset'].split('T')[1].split(":")[0]
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]

print(sunset)
time_now = datetime.now()