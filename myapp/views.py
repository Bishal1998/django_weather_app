from django.http.response import HttpResponse
from django.shortcuts import HttpResponse, render
import requests


# Create your views here.
def index(request):

    city = "Bharatpur"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},np&appid=5673ca857af8cd7aec37c89c31158e39'
    data = requests.get(url).json()
    payload = {
    'city':data['name'], 
    'country':data['sys']['country'], 
    'kelvin_temp':float(data['main']['temp']),
    'temp':int(data['main']['temp'] -273),
    'humidity':data['main']['humidity'],
    'visibility':data['visibility'],
    'speed':data['wind']['speed'],
    'condition':data['weather'][0]['description'],
    }
    context = {
        'payload':payload
    }

    return render(request, 'index.html', context)
