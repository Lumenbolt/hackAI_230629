import requests
from messages.temperature_data import TemperatureData

class TemperatureAlert:
    def __init__(self, key):
        self.weather_api_key = key

    def fetch_temperature_data(self, city):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            avg_temp = round(float(weather_data['main']['temp']) - 273.15, 3)
            return TemperatureData(city=city, temperature=avg_temp)