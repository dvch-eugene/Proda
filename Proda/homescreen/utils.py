import requests
from dotenv import load_dotenv
import os

class Weather():
    # Виджет погоды на главной странице
    def __init__(self, location=None):
        load_dotenv()
        self.celsius = 0
        self.location = location
        self.API_KEY = os.getenv('WEATHER_API_KEY')
        self.BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
        self.url = self.BASE_URL + 'appid=' + self.API_KEY + '&q=' + self.location
        self.weather = requests.get(self.url).json()

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def get_temperature(self, is_celsius=True):
        if is_celsius:
            return '{:.0f}'.format(self.weather['main']['temp'] - 273.15), '{:.0f}'.format(self.weather['main']['feels_like'] - 273.15)
        else:
            return '{:.0f}'.format(self.weather['main']['temp'] * (9/5) + 32),  '{:.0f}'.format(self.weather['main']['feels_like'] * (9/5) + 32)
        
    def get_weather_location(self):
        return self.weather['sys']['country'], self.weather['name']
    
    def get_humidity(self):
        return self.weather['main']['humidity']
    
    def get_weather_description(self):
        return self.weather['weather'][0]['main']
    
    def get_wind(self):
        return self.weather['wind']['speed']
        