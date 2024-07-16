import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import randint
API_TOKEN = '7021611244:AAH3ZTqRIcDQcfZk-jdiv2xXEPXK6Wf3FH8'
bot = telebot.TeleBot(API_TOKEN)

session = {}
@bot.message_handler(commands=['game'])
def send_message_game(message):
    chatID = message.from_user.id
    session[chatID]['rand'] = randint(1, 100)
    bot.send_message(chatID, 'Бот загадает число от 1 до 100. Ваша цель его отгадать. На выполнение даётся 3 попытки.')
    bot.register_next_step_handler(message, first_try)

def first_try(message):
    chatID = message.from_user.id
    if int(message.text) == session[chatID]['rand']:
        bot.send_message(chatID,'Вы отдагали число с первой попытки. ')
    elif int(message.text) > session[chatID]['rand']:
        bot.send_message(chatID, 'Вы ввели число больше загаданного. Осталось 2 попытки')
        bot.register_next_step_handler(message, second_try)
    elif int(message.text) < session[chatID]['rand']:
        bot.send_message(chatID, 'Вы ввели число меньше загаданного. Осталось 2 попытки')
        bot.register_next_step_handler(message, second_try)

def second_try(message):
    chatID = message.from_user.id
    if int(message.text) == session[chatID]['rand']:
        bot.send_message(chatID,'Вы отдагали число со второй попытки.')
    elif int(message.text) > session[chatID]['rand']:
        bot.send_message(chatID, 'Вы ввели число больше загаданного. Осталась 1 попытка.')
        bot.register_next_step_handler(message, third_try)
    elif int(message.text) < session[chatID]['rand']:
        bot.send_message(chatID, 'Вы ввели число меньше загаданного. Осталась 1 попытка.')
        bot.register_next_step_handler(message, third_try)

def third_try(message):
    chatID = message.from_user.id
    if int(message.text) == session[chatID]['rand']:
        bot.send_message(chatID,'Вы отдагали число с третьей попытки.')
    else:
        bot.send_message(chatID, 'Повезёт в другой раз.')

def create_markup(list_buttons):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in list_buttons:
        markup.add(i)
    return markup


@bot.message_handler(commands=['buttons'])
def buttons(message):
    chat_ID = message.from_user.id
    markup = create_markup(['Кнопка 1', 'Кнопка 2','Кнопка 3','Кнопка 4','Кнопка 5'])
    bot.send_message(chat_ID, 'Набор кнопок', reply_markup=markup)

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

@bot.message_handler(commands=['knopki'])
def knopki(message):
    chatID = message.from_user.id
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Мем', callback_data='meme')
    button2 = InlineKeyboardButton('Картинка', callback_data='image')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(chatID, 'Выберите изображение', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:True)
def handle_callback(callback):
    chatID = callback.from_user.id
    button_call = callback.data
    if button_call == 'meme':
        bot.send_photo(chatID,'https://icdn.lenta.ru/images/2023/10/17/22/20231017220531545/square_320_5b95c890f906452b293c849e3fe60413.jpg')
    elif button_call == 'image':
        bot.send_photo(chatID, 'https://lifehacker.ru/special/fujifilm/dist/static/img/5.2410a2d.jpg')


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