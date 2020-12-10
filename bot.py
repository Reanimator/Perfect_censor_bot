__author__ = 'Агеев Михаил Михайлович'

import telebot
import re
# from telebot import *

bot = telebot.TeleBot('1307629489:AAHHuncuzhr__UbKHvds1o737T4p2-eHZMw')
arr = []


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    for i in re.split('[^\w]', message.text):
        if len(i.split('_')) > 1:
            pass
        else:
            arr.append(i)
    print(arr)



bot.polling(none_stop=True, interval=0)
