from time import sleep

import requests

import json
from config import *






#city to query
target_city = 'Nairobi'
BASE_URL = "http://api.weatherstack.com/current"
headers = {
    'user-agent':
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
}


def getCurrentWeather(url, city, api_key, my_headers):
    '''Get the current weather from Weatherstack API'''
    querystring = {"access_key": api_key, "query": city}
    #query the current weather with the  provided querystring
    response = requests.request("GET",
                                url,
                                params=querystring,
                                headers=my_headers)
    #convert response to json object from received string 
    current_weather = response.json()
    print("current_weather data received")
    #return the converted  results
    return current_weather





def sendToRabbitMq(channel, q_name, message_body):
    '''Send message body to RabbitMq channel'''
    channel.basic_publish(exchange='',
                      routing_key=q_name,
                      body=message_body)
    print("Sent to rabbitmq")
    

    
    
    
#while loop to get the weather data.
while True:
    try:
        
        current_weather_data= getCurrentWeather(BASE_URL, target_city, ACCESS_KEY, headers)
        #pause the loop for 10 minutes
        
        #send our data to RabbitMQ qeuee
        sendToRabbitMq(channel=nairobi_channel, q_name='lendxs', message_body=json.dumps(current_weather_data))
        sleep(6)
    except Exception as error:
        #print out error is we get any
        print(error)
        
        

    