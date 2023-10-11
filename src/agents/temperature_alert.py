#importing the 'requests' library to make HTTP requests and the 'TemperatureData' class from the 'temperature_data' module
import requests
from messages.temperature_data import TemperatureData

#define a class named 'TemperatureAlert' to fetch temperature data from an external weather API
class TemperatureAlert:
    # The class constructor takes an API key as a parameter
    def __init__(self, key):
        self.weather_api_key = key

    # to fetch the temperature data for a given city and return it as a 'TemperatureData' object
    def fetch_temperature_data(self, city):

        # build the URL for the weather API request using the provided API key and the specified city
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}'

        # send an HTTP GET request to the API
        response = requests.get(url)

         # check if the response status code indicates success (status code 200)
        if response.status_code == 200:

             # parse the JSON response to extract weather data, including temperature
            weather_data = response.json()

            # calculate the average temperature in Celsius and round it to 3 decimal places
            avg_temp = round(float(weather_data['main']['temp']) - 273.15, 3)
            
            # create a 'TemperatureData' object with the city and temperature, and return it
            return TemperatureData(city=city, temperature=avg_temp)