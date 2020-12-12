from requests import get
from json import dumps
weather = 'https://api.openweathermap.org/data/2.5/weather'
onecall = 'https://api.openweathermap.org/data/2.5/onecall'
token = '801db4d874c0fd13fadef4c681a48929'

method = input('Что вы хотите узнать? (Погоду/Прогноз): ')
if method == 'Погоду':
    city_name = input('Название города: ')
    json = get(weather, {
        'q': city_name,
        'appid': token,
        'units': 'metric',
        'lang': 'ru'
    }).json()

    while 'main' not in json:
        print('Город не найден')
        city_name = input('Название города: ')
        json = get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2f22a7569578901533a5ec9cef699258').json()

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
elif method == 'Прогноз':
    lat = float(input('Введите широту: '))
    lon = float(input('Введите долготу: '))
    json = get(onecall, {
        'lat': lat,
        'lon': lon,
        'appid': token,
        'units': 'metric',
        'lang': 'ru',
        'exclude': 'current,minutely,hourly,alerts'
    }).json()

    day = 0
    daily = json['daily']
    for forecast in daily:
        day += 1
        print('-' * 25)
        print(f'через {day} дней')
        temp = daily['temp']
        temp_day = temp['day']
        temp_night = temp['night']
        temp_eve = temp['eve']
        temp_morn = temp['morn']
        print(f'Утро: {temp_morn}, День: {temp_day}, Вечер: {temp_eve}, Ночь: {temp_night}')

    print(dumps(json, indent=2))
else:
    print('Ошибка')
    exit(1)




