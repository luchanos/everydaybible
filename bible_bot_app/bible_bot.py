import telebot
from bible_bot_app.main_commands import give_jesus, give_start_of_bible, give_indulgence, bless_me
from bible_bot_app.settings import TOKEN

bot = telebot.TeleBot(TOKEN)


commands = {'give_jesus': give_jesus,
            'give_start_of_bible': give_start_of_bible,
            'give_indulgence': give_indulgence,
            'bless_me': bless_me}


@bot.message_handler(commands=list(commands.keys()))
def command_router(message):
    content = message.json
    command_to_execute = content['text'].split('@')[0][1:]
    commands[command_to_execute](message, bot)


if __name__ == '__main__':
    bot.polling(none_stop=True)
