from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
b0 = InlineKeyboardButton('Регестрация', callback_data='register')
b1 = InlineKeyboardButton('Информация об услугах', callback_data='info')
b2 = InlineKeyboardButton('Заказать', callback_data='call')
b3 = InlineKeyboardButton('Назад в меню', callback_data='back')
b4 = InlineKeyboardButton('Нет ',callback_data='register')
b5 = InlineKeyboardButton('Да',callback_data='info')
prikol = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b1)
rofl = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(b2).row(b3)
superrofl = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b3)
superultrarofl = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b4).add(b5)
admin = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(b1).add(b2, b0)