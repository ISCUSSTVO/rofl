from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
y1 = InlineKeyboardButton('Первая уборка', callback_data='first')
y2 = InlineKeyboardButton('Вторая уборка', callback_data='second')
y3 = InlineKeyboardButton('Третья уборка', callback_data='third')
asd = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(y1, y2).row(y3)