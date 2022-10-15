from aiogram.dispatcher.filters import Text
from aiogram import types
from loader import dp

@dp.message_handler(Text(equals='Случайные данные', ignore_case=True))
