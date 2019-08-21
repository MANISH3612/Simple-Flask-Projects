import requests
def weather(city):
    base = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f37ab6c03e97e9ba893f5fde006d990d&units=metric"
    r = requests.get(base).json()
    r['city'] = city
    return r