from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
y1 = InlineKeyboardButton('Первая уборка', callback_data='www')
y2 = InlineKeyboardButton('Вторая уборка', callback_data='www')
y3 = InlineKeyboardButton('Третья уборка', callback_data='www')
asd = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(y1, y2).row(y3)