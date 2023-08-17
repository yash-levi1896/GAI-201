from django.test import TestCase , Client
from django.urls import reverse
from . import views
# Create your tests here.


class WeatherViewTest(TestCase):
    def test_valid_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'temperature': 14, 'weather': 'Cloudy'})
        print(response.status_code)
        print(str(response.content, encoding='utf8'))
    def test_invalid_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'InvalidCity'}))
        self.assertEqual(response.status_code, 404)

    def test_add_weather_data(self):
        
        data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'}
        response = self.client.post(reverse('weather_list'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)  # 201 Created
        # Check if the data was actually added
        self.assertIn('Chicago', views.weather_data)  # Make sure 'Chicago' is correctly used here
        self.assertEqual(views.weather_data['Chicago']['temperature'], 18)
        self.assertEqual(views.weather_data['Chicago']['weather'], 'Cloudy') 

    def test_delete_weather_data(self):
      city_to_delete = 'Seattle'
      response = self.client.delete(reverse('weather_delete', args=[city_to_delete]))
      self.assertEqual(response.status_code, 204)  # 204 No Content
      test_weather_data = views.weather_data.copy()
      # Check if the data was actually deleted
      self.assertNotIn(city_to_delete, test_weather_data)
    
    def test_update_weather_data(self):
      city_to_update = 'Austin'
      updated_data = {'temperature': 15, 'weather': 'Sunny'}
      test_weather_data = views.weather_data.copy()
      response = self.client.put(reverse('weather_detail', args=[city_to_update]), updated_data, content_type='application/json')
      self.assertEqual(response.status_code, 200)  # 200 OK
      

      # Check if the data was actually updated
      self.assertEqual(test_weather_data[city_to_update]['temperature'], updated_data['temperature'])
      self.assertEqual(test_weather_data[city_to_update]['weather'], updated_data['weather'])
