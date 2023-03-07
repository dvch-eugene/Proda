from django.urls import path, include
from .views import *
urlpatterns = [
    path('', HomeScreen.as_view(), name='homescreen'),
]
