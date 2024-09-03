import requests
import json
city = input("enter city :- ")


url ="https://api.weatherapi.com/v1/current.json?key=f6026d8544084f08a8270106243008&q="+city

df = requests.get(url)

data = json.loads(df.content)

print(city,data["location"]["region"],data["location"]["country"])
print(data["current"]["temp_c"])
print(data["current"]["temp_f"])
print(data["current"]["wind_kph"])