from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
b1 = KeyboardButton('/Регестрация')
b2 = KeyboardButton('/Лист')
b3 = KeyboardButton('/Удалить')

button_case_regestration = ReplyKeyboardMarkup(resize_keyboard=True).add(b1)\
    .add(b2).add(b3)