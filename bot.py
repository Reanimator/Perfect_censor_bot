__author__ = 'Агеев Михаил Михайлович'

import telebot
import re
# from telebot import *
from matlib import mat

bot = telebot.TeleBot('1307629489:AAHHuncuzhr__UbKHvds1o737T4p2-eHZMw')
arr = []


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    print('получение')
    for word in re.split(r'[^\w]', message.text):
        if len(word.split('_')) > 1:
            for part_word in word.split('_'):
                arr.append(part_word)
        else:
            arr.append(word)
    for i in arr:
        if i in mat():
            bot.delete_message(message.chat.id, message.message_id)
            if message.chat.title is None:
                bot.send_message(
                    message.from_user.id,
                    text=f'Вы хомите боту )')
            else:
                bot.send_message(
                    message.from_user.id,
                    text=f'Ваше сообщение из чата {message.chat.title} удалено из-за слова {i}')
            print('удаление')


bot.polling(none_stop=True, interval=0)
