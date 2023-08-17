from django.urls import path
from . import views

urlpatterns=[
    path('weather/<str:city>/', views.weather_view, name='weather'),
    path('weather', views.add_weather_data, name='weather_list'),
     path('weather/delete/<str:city>/', views.delete_weather_data, name='weather_delete'),
     path('weather/update/<str:city>/', views.update_weather_data, name='weather_detail'),
]