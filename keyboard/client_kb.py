from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
b1 = KeyboardButton('/Информация_об_услугах')
b2 = KeyboardButton('/Заказ_услуги')
prikol = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(b1).add(b2)