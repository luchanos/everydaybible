import telebot
from settings import TOKEN
bot = telebot.TeleBot(TOKEN)


if __name__ == '__main__':
    bot.polling(none_stop=True)
