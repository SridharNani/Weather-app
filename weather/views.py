from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    city=request.GET.get('city','Lucknow')
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=35cdeedf85fc93c9c85649aa81333b73'
    data=requests.get(url).json()

    payload={
            'city':data['name'],
            'weather':data['weather'][0]['main'],
            'icon':data['weather'][0]['icon'],
            'kelvin_temprature':data['main']['temp'],
            'celcius_temprature':int(data['main']['temp']-273),
            'pressure':data['main']['pressure'],
            'humidty':data['main']['humidity'],
            'description':data['weather'][0]['main']
    }

    context = {'data': payload}
    return render(request,'home.html',context)