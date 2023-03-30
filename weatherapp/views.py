from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup as bs

def get_weather_data(city):
    city = city.strip().replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    session = requests.Session()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    language = "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,bg;q=0.6"
    session.headers['user-agent'] = user_agent
    session.headers['accept-language'] = language
    response = session.get(url)
    soup = bs(response.text,'html.parser')
    # Extract region Data

    result = {}
    region = soup.find('div',{'class':'vqkKIe wHYlTd'}).find('span',{'class':'BBwThe'}).text
    day_time = soup.find('div',{'id':'wob_dts'}).text
    weather = soup.find('span',{'id':'wob_dc'}).text
    temp = soup.find('span',{'id':'wob_tm'}).text
    result['region'] = region
    result['day_time'] = day_time
    result['weather'] = weather
    result['temp'] = temp
    return result

def home_view(request):
    if request.method == "GET" and 'city' in request.GET:
        city = request.GET.get('city')
        result = get_weather_data(city)
        context = {'results': result}
    else:
        context = {}

    return render(request, 'weatherapp/index.html', context)