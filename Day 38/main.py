import os
import requests
from datetime import datetime

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_URL = "https://api.sheety.co/83241c05a9a5d1f00c0da390ee982e77/myWorkouts/workouts"
SHEETY_HEADER = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer " + SHEETY_TOKEN
}

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_TOKEN = os.environ.get("NUTRITIONIX_TOKEN")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_HEADER = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_TOKEN
}
EXERCISE_QUERY = {
    "query": "Swam for 1 h"
}

def create_query() -> dict:
    query = input("What did you do?\n")
    return {"query": query}

def get_exercise_data(query: dict):
    response = requests.post(url=EXERCISE_ENDPOINT, json=query, headers=EXERCISE_HEADER)
    response.raise_for_status()
    return response.json()

def add_data_in_spreadsheet(json):
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    for exercise in json['exercises']:
        data = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise['user_input'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
        }
        response = requests.post(url=SHEETY_URL, json=data, headers=SHEETY_HEADER )
        response.raise_for_status()

while True:
    my_query = create_query()
    data = get_exercise_data(my_query)
    # data = {'exercises': [{'tag_id': 100, 'user_input': 'walk', 'duration_min': 45, 'met': 3.5, 'nf_calories': 183.75, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None}]}
    add_data_in_spreadsheet(data)



