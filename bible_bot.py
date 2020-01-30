import telebot
import time
import os

from bible_parser import bible_parser
from settings import TOKEN, PATH_TO_ICONS
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['give_jesus'])
def find_file_ids(message):
    for file in os.listdir(path=PATH_TO_ICONS):
        if file.split('.')[-1] == 'jpg':
            f = open(PATH_TO_ICONS + file, 'rb')
            bot.send_photo(message.chat.id, f)
        time.sleep(1)


def full_name_getter(message):
    name = message.from_user.first_name
    surname = message.from_user.last_name
    if not name:
        name = ''
    if not surname:
        surname = ''
    return f"{name} {surname}"


@bot.message_handler(commands=['bless_me'])
def find_file_ids(message):
    answer = f"Благословляю тебя, {full_name_getter(message=message)}"
    bot.send_message(chat_id=message.chat.id, text=answer)


@bot.message_handler(commands=['give_indulgence'])
def find_file_ids(message):
    answer = f"Твои грехи отпущены, {full_name_getter(message=message)}"
    bot.send_message(chat_id=message.chat.id, text=answer)


@bot.message_handler(commands=['give_start_of_bible'])
def find_file_ids(message):
    answer = bible_parser()
    bot.send_message(chat_id=message.chat.id, text=answer)


if __name__ == '__main__':
    bot.polling(none_stop=True)
