from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from geopy.geocoders import Nominatim

from .utils import *


class HomeScreen(TemplateView):
    template_name = 'homescreen/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_title'] = ''

        location = ''
        
        ip = self.request.META.get('REMOTE_ADDR', None) 
        # won't work at localhost, 'cause gets localhost ip - 127.0.0.1
        if ip:
            location = requests.get(f'https://api.iplocation.net/?cmd=ip-country&ip={ip}').json()['country_name']
        else:
            location = 'Minsk' # default city

        weather = Weather('Minsk')
        weather.get_temperature(is_celsius=True)
        context['temperature'], context['temp_feels_like'] = weather.get_temperature()
        context['weather_country'], context['weather_city'] = weather.get_weather_location()
        context['humidity'] = weather.get_humidity()
        context['weather_description'] = weather.get_weather_description()
        context['wind'] = weather.get_wind()
        return context
