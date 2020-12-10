__author__ = 'Агеев Михаил Михайлович'

import telebot
from telebot import *

bot = telebot.TeleBot('1307629489:AAHHuncuzhr__UbKHvds1o737T4p2-eHZMw')


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    pass
