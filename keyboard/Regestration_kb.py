from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
b1 = InlineKeyboardButton('Регестрация', callback_data='register')


button_case_regestration = InlineKeyboardMarkup(resize_keyboard=True).add(b1)