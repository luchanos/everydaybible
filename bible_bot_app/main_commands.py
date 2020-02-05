import os
import time
from bible_bot_app.bible_parser import bible_parser
from bible_bot_app.settings import PATH_TO_ICONS
from bible_bot_app.utils import full_name_getter


def bless_me(message, bot):
    answer = f"Благословляю тебя, {full_name_getter(message=message)}"
    bot.send_message(chat_id=message.chat.id, text=answer)


def give_indulgence(message, bot):
    answer = f"Твои грехи отпущены, {full_name_getter(message=message)}"
    bot.send_message(chat_id=message.chat.id, text=answer)


def give_start_of_bible(message, bot):
    answer = bible_parser()
    bot.send_message(chat_id=message.chat.id, text=answer)


def give_jesus(message, bot):
    for file in os.listdir(path=PATH_TO_ICONS):
        if file.split('.')[-1] == 'jpg':
            f = open(PATH_TO_ICONS + file, 'rb')
            bot.send_photo(message.chat.id, f)
        time.sleep(1)