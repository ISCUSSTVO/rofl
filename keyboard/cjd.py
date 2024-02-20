from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
y1 = InlineKeyboardButton('Поддерживающая уборка', callback_data='first')
y2 = InlineKeyboardButton('Гениральная уборка', callback_data='second')
y3 = InlineKeyboardButton('Комплексная уборка', callback_data='third')
asd = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(y1, y2).row(y3)