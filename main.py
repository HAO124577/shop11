from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot ('6514299012:AAH7o-MbQ7DAEB9wNCgUxK1YMy9xLuQ--AI')
dp = Dispatcher(bot)

@dp.message_handler (commands=[ 'start'])
async def start (message: types. Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть страницу', web_app=WebAppInfo(url='https://hao124577.github.io/1111/')))
    await message.answer('Дривет, мой друг!', reply_markup=markup)

executor.start_polling(dp)