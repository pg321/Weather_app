import requests
import json
import os


city = input("Enter the name of your city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=ae94fd930d484c38866150234231809&q={city}"

r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
d = wdic["current"]["pressure_mb"]
c = wdic["current"]["wind_kph"]
p = wdic["current"]["precip_mm"]
h = wdic["current"]["humidity"]



os.system(f"espeak 'The current weather details in {city} is as following:'")
os.system(f"espeak '1.   temperature of {w} degrees'")
os.system(f"espeak '2.   Wind of {c} kilometer per hour'")
os.system(f"espeak '3.   Pressure of {d}'")
os.system(f"espeak '4.   precipitation of {p} millimeters'")
os.system(f"espeak '5.   Humidity of {h} gram per meter qube'")

