from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
bq = InlineKeyboardButton('На основной', callback_data='main')
bq1 = InlineKeyboardButton('Да', callback_data='main')
bx = InlineKeyboardButton('На другой', callback_data='twink')
bx1 = InlineKeyboardButton('Нет', callback_data='twink')
b0 = InlineKeyboardButton('Регестрация', callback_data='register')
ba = InlineKeyboardButton('Основное окно бота', callback_data='main_win')
b1 = InlineKeyboardButton('Информация об услугах', callback_data='info')
b11 = InlineKeyboardButton('Да', callback_data='info')
b2 = InlineKeyboardButton('Заказать', callback_data='call1')
bw = InlineKeyboardButton('Заказать', callback_data='call2')
be = InlineKeyboardButton('Заказать', callback_data='call3')
b3 = InlineKeyboardButton('Назад в меню', callback_data='back')
b4 = InlineKeyboardButton('Нет ',callback_data='register')
b5 = InlineKeyboardButton('Да',callback_data='info')
b6 = InlineKeyboardButton('иди нахуй', callback_data='dinaxuy')
b7 = InlineKeyboardButton('стерпеть', callback_data='sterpet')
qw7e8uh = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(bx1, bq1)
a9iokjk = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(bq,bx)
asdjk = InlineKeyboardMarkup(resize_keyboard = True)\
    .row(ba)
qwerts = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(b6, b7)
prikol = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b1)
rofl = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(b2).row(b3)
rofl1 = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(bw, b3)
rofl2 = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(be, b3)
superrofl = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b3)
superultrarofl = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b4).add(b5)
admin = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(b1).add(b2, b0, b3, b4, b5)