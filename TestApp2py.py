
# Import stuff
import json
import requests
from pprint import pprint

url = 'http://api.openweathermap.org/data/2.5/forecast'
#paramDict = {'q': 'London,UK', 'units': 'metric', 'appid': '4a6da2fb67e933bfe69b0fb23e33f26d', 'cnt': 5}
paramDict = {'q': 'Chicago,US', 'units': 'imperial', 'appid': '4a6da2fb67e933bfe69b0fb23e33f26d', 'cnt': 5}
response = requests.get(url, params=paramDict)
parsed_json = response.json();
pprint(parsed_json)