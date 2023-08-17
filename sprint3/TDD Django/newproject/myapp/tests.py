from django.test import TestCase
from django.urls import reverse

# Create your tests here.

weather_data = {
        'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
        'New York': {'temperature': 20, 'weather': 'Sunny'},
        'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
        'Seattle': {'temperature': 10, 'weather': 'Rainy'},
        'Austin': {'temperature': 32, 'weather': 'Hot'},
    }

class WeatherAPITest(TestCase):

    def test_add_weather_data(self):
        data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'}
        response = self.client.post(reverse('weather_list'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)  # 201 Created

        # Check if the data was actually added
        self.assertIn('Chicago', weather_data)
        self.assertEqual(weather_data['Chicago']['temperature'], 18)
        self.assertEqual(weather_data['Chicago']['weather'], 'Cloudy')