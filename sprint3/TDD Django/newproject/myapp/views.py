from django.shortcuts import render
import json
from django.http import HttpRequest,JsonResponse
# Create your views here.
weather_data = {
        'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
        'New York': {'temperature': 20, 'weather': 'Sunny'},
        'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
        'Seattle': {'temperature': 10, 'weather': 'Rainy'},
        'Austin': {'temperature': 32, 'weather': 'Hot'},
    }
def add_weather_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city = data.get('city')
        temperature = data.get('temperature')
        weather = data.get('weather')

        if city and temperature is not None and weather:
            weather_data[city] = {'temperature': temperature, 'weather': weather}
            return JsonResponse(weather_data[city], status=201)
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)