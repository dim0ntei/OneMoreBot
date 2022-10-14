from aiogram import Bot, Dispatcher, types
from data import config
bot = Bot(config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)