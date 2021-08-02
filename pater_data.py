#Создать патерные данные о погоде
import requests, json

URL_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=8ab8dd8e10c2a1ae46c279684b638c3e"
w = requests.get(URL_TEMPLATE)
dict =w.json()
s = dict["main"]
print("temp:", dict['main']['temp'])
