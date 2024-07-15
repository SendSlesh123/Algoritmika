import telebot

API_TOKEN = '7021611244:AAH3ZTqRIcDQcfZk-jdiv2xXEPXK6Wf3FH8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Hi!')

@bot.message_handler(commands=['help'])
def weee(message):
    print(message)

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, message.from_user.username)

@bot.message_handler(commands=['humor'])
def shutka(message):
    bot.reply_to(message, 'Буратино утонул')

@bot.message_handler(func=lambda message: True)
def echo(message):
    for symbol in message.text:
        bot.reply_to(message, symbol)

bot.infinity_polling()