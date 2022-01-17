from time import sleep
from dotenv import load_dotenv
import os
import requests

load_dotenv()
ACCESS_KEY = os.environ.get('APIKey')


#city to query
target_city = 'Nairobi'
BASE_URL = "http://api.weatherstack.com/current"
headers = {
    'user-agent':
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
}


def getCurrentWeather(url, city, api_key, my_headers):
    querystring = {"access_key": api_key, "query": city}
    #query the current weather with the  provided querystring
    response = requests.request("GET",
                                url,
                                params=querystring,
                                headers=my_headers)
    #convert response to json object from received string 
    current_weather = response.json()
    print(current_weather)
    #return the converted  results
    return current_weather

while True:
    try:
        getCurrentWeather(BASE_URL, target_city, ACCESS_KEY, headers)
        sleep(6)
    except Exception as error:
        print(error)
        