from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView


class HomeScreen(TemplateView):
    template_name = 'homescreen/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_title'] = ''
        return context
