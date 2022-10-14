from aiogram.dispatcher.filters import Text
from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}")


@dp.message_handler(Text(equals='О тебе', ignore_case=True))
async def about(message: types.Message):
    await message.answer('Я пока ничего не умею')

