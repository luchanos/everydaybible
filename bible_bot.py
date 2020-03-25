import telebot
from telebot import apihelper
from main_commands import give_jesus, give_indulgence, bless_me, pray_coronavirus
from settings import TOKEN, USE_PROXY, PROXY
from utils import supress_errors

if USE_PROXY:
    apihelper.proxy = {'https': f'socks5://{PROXY}'}

bot = telebot.TeleBot(TOKEN)

commands = {'give_jesus': give_jesus,
            'give_indulgence': give_indulgence,
            'bless_me': bless_me,
            # 'give_bible_range': give_bible_range}
            'pray_coronavirus': pray_coronavirus}


@bot.message_handler(commands=['bless_user'])
def bless_user(message):
    user = message.json['text'].split(' ')[1][1:]
    bot.send_message(reply_to_message_id=message.message_id, text='lol', chat_id=message.chat.id)


@bot.message_handler(commands=list(commands.keys()))
@supress_errors
def command_router(message):
    content = message.json
    command_to_execute = content['text'].split('@')[0][1:]
    commands[command_to_execute](message, bot)


if __name__ == '__main__':
    bot.polling(none_stop=True)
