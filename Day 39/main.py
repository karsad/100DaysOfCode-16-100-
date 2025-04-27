from data_manager import DataManager
from flight_search import FlightSearch

file_data = DataManager()
new_data = file_data.get_data()

flight_search = FlightSearch()

for city in new_data['prices']:
    index = new_data['prices'].index(city)
    city_data = flight_search.city_search(city['city'])
    new_data['prices'][index]['iataCode'] = city_data['data'][0]['iataCode']

file_data.update_data(new_data)
print(new_data)
