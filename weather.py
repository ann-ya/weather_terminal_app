import requests
import datetime

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "9a05b63243ab6d8b9556ea184ef38821"

city_input = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city_input.title()}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    conditions = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 1)
    feels_like = round(data['main']['feels_like'] - 273.15, 1)
    humidity = data['main']['humidity']
    wind = round(data['wind']['speed'], 2)
    pressure = data['main']['pressure']
    city_timezone = int(data['timezone'])
    sunset_utc = data['sys']['sunset']
    sunset_local = datetime.datetime.utcfromtimestamp(sunset_utc + city_timezone).strftime("%a %d-%m-%Y %H:%M:%S")
    sunrise_utc = data['sys']['sunrise']
    sunrise_local = datetime.datetime.utcfromtimestamp(sunrise_utc + city_timezone).strftime("%a %d-%m-%Y %H:%M:%S")

    
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Feels like:", feels_like, "°C")
    print("Conditions:", conditions)
    print("Humidity:", humidity, "%")
    print("Wind:", wind, "m/s")
    print("Pressure:", pressure, "hPa")
    print("Sunrise:", sunrise_local)
    print("Sunset:", sunset_local)
else:
    print("An error occurred")