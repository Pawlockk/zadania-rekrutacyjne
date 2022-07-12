import requests
import os

key = os.environ['key']
def weather(name):
  r = requests.get('http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no'.format(key,name))
  temp_c = r.json()["current"]["temp_c"]
  temp_k = temp_c + 273.15
  location_name = r.json()["location"]["name"]
  print("Temperatura dla {}: \n{} K".format(location_name,temp_k))

weather("London")
weather("Warsaw")
weather("New_York")