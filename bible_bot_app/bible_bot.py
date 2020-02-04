import telebot
from bible_bot_app.settings import TOKEN
from bible_bot_app.utils import full_name_getter
from bible_bot_app.bible_parser import bible_parser
import time
import os
from bible_bot_app.settings import PATH_TO_ICONS

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['bless_me'])
def bless_me(message):
    answer = f"Благословляю тебя, {full_name_getter(message=message)}"
    bot.send_message(chat_id=message.chat.id, text=answer)


@bot.message_handler(commands=['give_indulgence'])
def give_indulgence(message):
    answer = f"Твои грехи отпущены, {full_name_getter(message=message)}"
    bot.send_message(chat_id=message.chat.id, text=answer)


@bot.message_handler(commands=['give_start_of_bible'])
def give_start_of_bible(message):
    answer = bible_parser()
    bot.send_message(chat_id=message.chat.id, text=answer)


@bot.message_handler(commands=['give_jesus'])
def give_jesus(message):
    for file in os.listdir(path=PATH_TO_ICONS):
        if file.split('.')[-1] == 'jpg':
            f = open(PATH_TO_ICONS + file, 'rb')
            bot.send_photo(message.chat.id, f)
        time.sleep(1)


if __name__ == '__main__':
    bot.polling(none_stop=True)
