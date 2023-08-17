from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
# Create your views here.

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}



def weather_view(request, city):
    try:
        weather_info = weather_data[city]
        return JsonResponse(weather_info)
    except KeyError:
        raise Http404("City not found")