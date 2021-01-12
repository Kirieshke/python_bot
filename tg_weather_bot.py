import telebot
import requests
import json
from datetime import datetime
token = '1578503566:AAGaQ-hANiE2nAcfrLe9ABDvcyh54_1r55k'
api = 'a89085cd586bbb189a873abff0ec3455'


bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text']) 



def get_text_messages(message):
    
    k = 1.33322

    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + message.text +'&units=metric&appid=a89085cd586bbb189a873abff0ec3455'
     
    response = requests.get(url).json()
    temp = response['main']['temp']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']
    atmosphere = response['main']['pressure']

    desc = list(response['weather'])
    
    description = desc[0]['description']

    deg = response['wind']['deg']

    def wind_direction(deg):
        if deg >= 0 and deg <= 15:
            return "North"
        elif deg >= 16 and deg <= 85:
            return "North-east"
        elif deg >= 86 and deg <= 95:
            return "East"
        elif deg >= 95 and deg <= 170:
            return "South-east"
        elif deg >= 170 and deg <= 200:
            return "South"
        elif deg >= 201 and deg <= 260:
            return "South-West"
        elif deg >= 261 and deg <= 300:
            return "West"
        elif deg >= 301 and deg <= 345:
            return "North-west"
        elif deg >= 346 and deg <= 360:
            return "North"

     
    if message.text != 0: 
         bot.send_message(message.from_user.id, "Temperature in " + message.text +": "+ str(temp)+"°C\n" + 
                                                "Humidity in " + message.text +": "+ str(humidity)+"%\n" +
                                                "Wind in " + message.text +": "+wind_direction(deg)+" "+ str(wind)+ "m/s\n" +
                                                "Atmospere pressure in " + message.text +": "+ str(int(atmosphere/k))+"mm\n" + 
                                                "Also in " + message.text +": "+ description +"\n" )
    
         
    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0) 

