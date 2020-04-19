import time

import telebot
from telebot import apihelper

from image_worker import jesus_quote_image
from main_commands import give_jesus, give_indulgence, bless_me, pray_coronavirus
from settings import TOKEN, PROXY
from utils import supress_errors

if PROXY:
    apihelper.proxy = {'https': f'socks5://{PROXY}'}

bot = telebot.TeleBot(TOKEN)

commands = {'give_jesus': give_jesus,
            'give_indulgence': give_indulgence,
            'bless_me': bless_me,
            'pray_coronavirus': pray_coronavirus}


@bot.message_handler(commands=list(commands.keys()))
@supress_errors
def command_router(message):
    content = message.json
    command_to_execute = content['text'].split('@')[0][1:]
    commands[command_to_execute](message, bot)


@bot.message_handler(commands=['test'])
def jesus_quote(message):
    bot.send_message(message.chat.id, reply_to_message_id=message.message_id, text='Введи текст цитаты, дитя моё')


@bot.message_handler(commands=['next'])
def waiting_for_message(message):
    bot.send_message(chat_id=message.chat.id, text='test')


# словарь для хранения чуваков которые отправили цитату
user_ids_for_quoting = set()


@bot.message_handler(commands=['jesus_quote'])
def jesus_quote(message):
    """Бот принимает сообщение от пользователя и потом ожидает когда пользователь введёт цитату"""
    user_ids_for_quoting.add(message.from_user.id)
    bot.send_message(message.chat.id, reply_to_message_id=message.message_id, text='Введи текст цитаты, дитя моё')


@bot.message_handler(content_types=['text'])
def quote_message_handler(message):
    if message.from_user.id in user_ids_for_quoting:
        jesus_quote_image(top=message.text)
        f = open('temporary.png', 'rb')
        bot.send_photo(message.chat.id, f, reply_to_message_id=f"\"{message.message_id}\"", caption='Держи')
        user_ids_for_quoting.remove(message.from_user.id)


def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as err:
        bot.stop_polling()
        time.sleep(3)
        telegram_polling()


if __name__ == '__main__':
    telegram_polling()
