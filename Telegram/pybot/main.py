import telebot
from telebot import types
from settings import bot

@bot.message_handler(commands=['start'])
def lets_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Помощь')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Привет, с чем нужна помощь')

@bot.message_handler()
def get_message(message):
    match message.text:
        case 'Помощь':
            bot.send_message(message.chat.id,'Привет, с чем нужна помощь')


bot.polling(none_stop=True, interval=0)