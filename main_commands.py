import os
from bible_parser import bible_parser
from settings import PATH_TO_ICONS
from utils import full_name_getter


def image_answer_sender(answer, img_name, bot, message):
    for file in os.listdir(path=PATH_TO_ICONS):
        if file.split('.')[0] == img_name:
            f = open(PATH_TO_ICONS + file, 'rb')
            bot.send_photo(message.chat.id, f, reply_to_message_id=message.message_id, caption=answer)


def bless_me(message, bot):
    answer = f"Благословляю тебя, {full_name_getter(message=message)}"
    # bot.send_message(text='https://sun9-57.userapi.com/c855124/v855124788/1f8ee1/vdTFg3zC2KE.jpg' +
    #                       ' ' + answer, chat_id=message.chat.id)
    image_answer_sender(answer=answer, img_name='blessing', bot=bot, message=message)


def give_indulgence(message, bot):
    answer = f"Твои грехи отпущены, {full_name_getter(message=message)}"
    # bot.send_message(text='https://sun9-35.userapi.com/c855124/v855124788/1f8eea/egynrCEJFjg.jpg' +
    #                       ' ' + answer, chat_id=message.chat.id)
    image_answer_sender(answer=answer, img_name='sins', bot=bot, message=message)


def give_jesus(message, bot):
    answer = f"Спаситель зрит на тебя, {full_name_getter(message=message)}"
    # bot.send_message(text='https://sun9-43.userapi.com/c855124/v855124788/1f8ed2/XxhPpkG6Jzg.jpg' +
    #                       ' ' + answer, chat_id=message.chat.id)
    image_answer_sender(answer=answer, img_name='есус', bot=bot, message=message)


def parse_args(s: str):
    return s.split(' ')[1:]


def give_bible_range(message, bot):
    pic_url = 'https://www.pravmir.ru/wp-content/uploads/2017/08/bibliya-2.jpg'
    args = list(map(int, parse_args(message.text)))
    answer = bible_parser(start=args[0], end=args[1])
    bot.send_message(text=pic_url + ' ' + answer, chat_id=message.chat.id)
