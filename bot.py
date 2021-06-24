# -*- coding: utf8 -*-
import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps



bot = telebot.TeleBot("1844449729:AAE4ZEZtVbTd_hBlNxEUZ8qpMEtKXdkE5yQ")
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Укажите Ваш город')

@bot.message_handler(content_types=['text'])
def test(message):
 try:
	
    place = message.text
  		
    config_dict = get_default_config()
    config_dict['language'] = 'ru'


    owm = OWM('9c5b5dca2e59009a529fbae5c313e39b' , config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    t = w.temperature('celsius')  
    t1 = t["temp"] 
    t2 = t["feels_like"] 
    t3 = t["temp_max"] 
    t4 = t["temp_min"] 

    wi = w.wind()["speed"]

    humi = w.humidity

    cl = w.clouds


    st = w.status


    dt = w.detailed_status


    time = w.reference_time('iso')

 
    pr = w.pressure['press']

    vd = w.visibility_distance
   

    bot.send_message(message.chat.id, "В городе " + str(place) + " температура " +  str(t1) + "°C " + "\n" + "Ощущается как " + str(t2) + "°C " + "\n" + "Максимальная температура " + str(t3) + "°C" + "\n" + "Минимальная температура " + str(t4) + "°C" "\n" + "Скорость ветра: " + str(wi) + "м/c" + "\n" + "Влажность: " + str(humi) + "%" "\n" + "Облачность: " + str(cl) + " облака " + "\n" + "Status: " +str(st)+ "  → " + str(dt) + "\n" +  "Время " + str(time) + "\n" + "Давление: " + str(pr) + " мм.рт.ст.")
    #if t1 > 30:
        #bot.send_message(message.chat.id, "pizdets zhara")
 except:
            bot.send_message(message.chat.id,"Такой город не найден!")
            print(str(message.text),"- не найден")        



bot.polling(none_stop=True, interval=0)
