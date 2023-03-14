from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .utils import *
from notes.models import Note


class HomeScreen(DataMixin, TemplateView):
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
            pass

        weather = Weather(location)

        c_def = self.get_weather_context(weather_obj=weather)

        context['notes_left'] = Note.objects.filter(owner=self.request.user.pk).order_by('id')[:3]
        context['notes_right'] = Note.objects.filter(owner=self.request.user.pk).order_by('id')[3:6]
        return dict(list(context.items())+list(c_def.items()))
