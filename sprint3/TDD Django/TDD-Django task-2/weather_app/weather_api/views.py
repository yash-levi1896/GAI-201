from django.shortcuts import render
from django.http import Http404,HttpResponse,JsonResponse
import json
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
    
def delete_weather_data(request, city):
    if request.method == 'DELETE':
        if city in weather_data:
            del weather_data[city]
            return HttpResponse(status=204)  # 204 No Content
        else:
            return JsonResponse({'error': 'City not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
    
def update_weather_data(request, city):
    if request.method == 'PUT':
        data = json.loads(request.body)
        if city in weather_data:
            weather_data[city]['temperature'] = data.get('temperature', weather_data[city]['temperature'])
            weather_data[city]['weather'] = data.get('weather', weather_data[city]['weather'])
            return JsonResponse(weather_data[city], status=200)
        else:
            return JsonResponse({'error': 'City not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
