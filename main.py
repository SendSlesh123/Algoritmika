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
    chat_ID = message.from_user.id
    bot.send_message(chat_ID, 'Буратино утонул')

@bot.message_handler(commands=['random1'])
def random1(message):
    chatID = message.from_user.id
    bot_message = bot.send_dice(chatID, '🎰')
    print(bot_message.dice.value)


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    chatID = message.from_user.id
    bot.send_sticker(chatID, 'CAACAgIAAxkBAAJlrWaWSicFqxKLZxr4EA7S-VlNzmJVAAJ7DQACK-uISrOE001rp6qDNQQ')

@bot.message_handler(commands=['doc'])
def send_doc(message):
    chatID = message.from_user.id
    bot.send_document(chatID, open('test_algoritmika.txt', 'rb'))

@bot.message_handler(commands=['location'])
def send_loc(message):
    chatID = message.from_user.id
    bot.send_location(chatID, 25.478504, 6.759766)
    bot.send_photo(chatID, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwObRKmsvn7XAnigQw3nsSTvM4t7E1g31C1Q&s')
    bot.send_photo(chatID, open('5237769070978392725.jpg', 'rb'))

@bot.message_handler(commands=['audio'])
def send_audio(message):
    chatID = message.from_user.id
    bot.send_audio(chatID,'https://zvukipro.com/uploads/files/2024-07/1720870718_ost_the_grand_duel_parte_prima_luis_bacalov.mp3')


@bot.message_handler(func=lambda message: True)
def echo(message):
    for symbol in message.text:
        bot.reply_to(message, symbol)

bot.infinity_polling()