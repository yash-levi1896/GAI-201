from django.urls import path
from . import views

urlpatterns = [
    path('weather', views.add_weather_data, name='weather_list'),
]