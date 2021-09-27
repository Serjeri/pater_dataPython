#Создать патерные данные о погоде
import requests, json

URL_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid="
w = requests.get(URL_TEMPLATE)
dict =w.json()
s = dict["main"]
print("temp:", dict['main']['temp'])
