import telebot
from telebot import apihelper
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


def waiting_for_message(message):
    bot.send_message(chat_id=message.chat.id, text='test')


@bot.message_handler(commands=['jesus_quote'])
def jesus_quote(message):
    bot.send_message(message.chat.id, reply_to_message_id=message.message_id, text='Введи текст цитаты, дитя моё')
    bot.register_next_step_handler(message=message, callback=waiting_for_message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
