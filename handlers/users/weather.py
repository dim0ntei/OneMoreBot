from aiogram.dispatcher.filters import Text
from data import keyboards
from aiogram import types
from loader import dp
from handlers import fsm


@dp.message_handler(Text(equals="Прогноз погоды", ignore_case=True))
async def weather_first(message: types.Message):
    await fsm.WatherState.now.set()
    await message.answer("Погода в каком месте вас интересует?", reply_markup=keyboards.geo)


@dp.message_handler(state=fsm.WatherState.now)
async def weather_second(message: types.Message):
    await message.answer(message.text)
