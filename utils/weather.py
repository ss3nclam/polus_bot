from configparser import ConfigParser

import requests


config = ConfigParser()
config.read('config.conf')
appid, city_id, lang = [param[1] for param in config.items('OPEN_WEATHER_API')]

ICONS = {'01':'☀️', '02':'🌤', '03':'⛅️', '04':'☁️', '09':'🌧', '10':'🌦', '11':'🌩', '13':'❄️', '50':'💨'}


def get():
    try:
        request = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'id': city_id, 'units': 'metric', 'lang': lang, 'APPID': appid})
        answer = request.json()
        temp = round(answer['main']['temp'])
        status = '' if 5 <= temp <= 25 else ('❄️ ' if temp < 5 else '🔥 ')
        conditions = answer['weather'][0]['description']
        icon = ICONS[answer['weather'][0]['icon'][:-1]]
        temp_min, temp_max = round(answer['main']['temp_min']), round(answer['main']['temp_max'])
        return f'{status}{temp}° {icon} {conditions} ↓{temp_min}° ↑{temp_max}°'
    
    except Exception:
        return '⚠️ Ошибка подключения к погодному серверу'
