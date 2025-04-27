import os
import requests

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_KEY")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        self._token = self.get_new_token()

    def get_new_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response =  requests.post(url=url, headers=header, data=body)
        response.raise_for_status()
        return response.json()['access_token']

    def city_search(self, city_name):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=url,
            headers=headers,
            params=query
        )
        return response.json()

