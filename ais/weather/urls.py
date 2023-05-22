from django.urls import path
from . import views


urlpatterns = [
    path('weather/weather.html', views.weather, name='weather'),
]