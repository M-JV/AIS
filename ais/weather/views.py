from django.shortcuts import render
from django.http import HttpResponse
import requests

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')  # Get the city from the form submission
    else:
        city = 'Pathanamthitta'  # Default city if no form submission

    api_key = 'd0eb75cf5f3c4d62311cb94a63774801'  # Replace with your OpenWeather API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp'] - 273.15  # Convert temperature from Kelvin to Celsius
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        context = {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'weather_description': weather_description
        }

        return render(request, 'weather/weather.html', context)
    else:
        return HttpResponse("Failed to retrieve weather information.")
