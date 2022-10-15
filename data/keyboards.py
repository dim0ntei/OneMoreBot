from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Обычные кнопки
settings = KeyboardButton(text="Настройки")
random_data = KeyboardButton(text="Случайные данные")
weather = KeyboardButton(text="Прогноз погоды")
geo_button_here = KeyboardButton(text="Погода у меня", request_location=True)
geo_button_where = KeyboardButton(text="Погода в другом месте")
back = KeyboardButton(text="Назад")

# Обычные клавиатуры
main_menu = ReplyKeyboardMarkup(one_time_keyboard=True,
                                resize_keyboard=True).add(random_data).row(weather, settings)
geo = ReplyKeyboardMarkup(one_time_keyboard=True,
                          resize_keyboard=True).add(geo_button_here).row(geo_button_where).add(back)
# Инлайн кнопки


# Инлайн клавиатуры

