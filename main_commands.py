import os
from settings import PATH_TO_ICONS
from utils import full_name_getter


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
    answer = f"Спаситель зрит на тебя, {full_name_getter(message=message)}"
    image_answer_sender(answer=answer, img_name='есус', bot=bot, message=message)


def pray_coronavirus(message, bot):
    answer = "Господи Боже наш, не вниди в суд с рабы Твоими, " \
             "и огради нас от губительнаго поветрия на ны движимаго." \
             " Пощади нас смиренных и недостойных рабов Твоих в покаянии" \
             " с теплою верою и сокрушением сердечным к Тебе милосердному" \
             " и благопременительному Богу нашему припадающих и на милость" \
             " Твою уповающих. Твое бо есть, еже миловати и спасати ны, " \
             "Боже наш, и Тебе славу возсылаем, Отцу и Сыну и Святому Духу," \
             " ныне и присно и во веки веков. Аминь."
    image_answer_sender(answer=answer, img_name='coronavirus', bot=bot, message=message)
