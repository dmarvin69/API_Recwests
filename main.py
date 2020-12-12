from requests import get
from json import dumps
weather = 'https://api.openweathermap.org/data/2.5/weather'
token = '801db4d874c0fd13fadef4c681a48929'
city_name = input('Название города: ')
json = get(weather,{
           'q':city_name,
           'appid':token,
           'units':'metric',
           'lang':'ru'
}).json()


while 'main' not in json:
 print('Город не найден')
 city_name = input('Название города: ')
 json = get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2f22a7569578901533a5ec9cef699258').json()


temp = json['main']['temp']
feels_like = json['main']['feels_like']
humidity = json['main']['humidity']
pressure = round(json['main']['pressure'] * 0.750064)
weathers = json['weather']

print(f'температура в городе {city_name}:{temp}, ощущается как: {feels_like}')
print(f'Влажность: {humidity}')
print(f'Давление: {pressure} мм ртутного столба')
for w in weathers:
 print(f'Погода: {w["description"]}')

