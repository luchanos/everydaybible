import os
from bible_bot_app.bible_parser import bible_parser
from bible_bot_app.settings import PATH_TO_ICONS
from bible_bot_app.utils import full_name_getter


def image_answer_sender(answer, img_name, bot, message):
    for file in os.listdir(path=PATH_TO_ICONS):
        if file.split('.')[0] == img_name:
            f = open(PATH_TO_ICONS + file, 'rb')
            bot.send_photo(message.chat.id, f, reply_to_message_id=message.message_id, caption=answer)


def bless_me(message, bot):
    answer = f"Благословляю тебя, {full_name_getter(message=message)}"
    image_answer_sender(answer=answer, img_name='blessing', bot=bot, message=message)


def give_indulgence(message, bot):
    answer = f"Твои грехи отпущены, {full_name_getter(message=message)}"
    image_answer_sender(answer=answer, img_name='sins', bot=bot, message=message)


def give_jesus(message, bot):
    for file in os.listdir(path=PATH_TO_ICONS):
        if file.split('.')[0] == 'есус':
            f = open(PATH_TO_ICONS + file, 'rb')
            bot.send_photo(message.chat.id, f)


def parse_args(s: str):
    return s.split(' ')[1:]


def give_bible_range(message, bot):
    pic_url = 'https://www.pravmir.ru/wp-content/uploads/2017/08/bibliya-2.jpg'
    args = list(map(int, parse_args(message.text)))
    answer = bible_parser(start=args[0], end=args[1])
    bot.send_message(text=pic_url + ' ' + answer, chat_id=message.chat.id)
