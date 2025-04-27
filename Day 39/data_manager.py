import requests
import os

class DataManager:
    def __init__(self):
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_URL = "https://api.sheety.co/83241c05a9a5d1f00c0da390ee982e77/flightDeals/prices"
        self.SHEETY_HEADER = {"Authorization": "Bearer " + self.SHEETY_TOKEN}
        self.data = self.read_file()

    def get_data(self):
        return self.data

    def read_file(self):
        response = requests.get(url=self.SHEETY_URL, headers=self.SHEETY_HEADER)
        response.raise_for_status()
        return response.json()

    def update_data(self, data):
        self.write_data(data)
        self.data = data

    def write_data(self, data):
        for row in data['prices']:
            row_url = self.SHEETY_URL + '/' + str(row['id'])
            row_data = {'price': {'city': row['city'], 'iataCode': row['iataCode'], 'lowestPrice': row['lowestPrice']}}
            response = requests.put(url=row_url, json=row_data, headers=self.SHEETY_HEADER)
            response.raise_for_status()