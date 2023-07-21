from settings import bot as bt, url_web
from aiogram.types.web_app_info import WebAppInfo
from aiogram import Dispatcher, executor, types

bot = Dispatcher(bt)

@bot.message_handler(commands=['start'])
async def lets_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Web app', web_app=WebAppInfo(url = url_web)))
    markup.add(types.KeyboardButton('О нас', web_app=WebAppInfo(url=url_web)))
    await message.answer('Привет!', reply_markup=markup)




executor.start_polling(bot)