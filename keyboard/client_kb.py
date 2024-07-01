from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
bq = InlineKeyboardButton(text='На основной', callback_data='info')
login = InlineKeyboardButton('Вход', callback_data='login')
bq1 = InlineKeyboardButton(text='Да', callback_data='main_win')
asdh = InlineKeyboardButton(text='Да', callback_data='dermo')
asd2h = InlineKeyboardButton(text='Нет', callback_data='call1')
asd5h = InlineKeyboardButton(text='Нет', callback_data='call2')
asd12h = InlineKeyboardButton(text='Нет', callback_data='call3')
bx = InlineKeyboardButton(text='На другой', callback_data='twink')
bx1 = InlineKeyboardButton(text='Нет', callback_data='twink')
b0 = InlineKeyboardButton(text='Регестрация', callback_data='register')
ba = InlineKeyboardButton(text='Основное окно бота', callback_data='main_win')
b1 = InlineKeyboardButton(text='Информация об услугах', callback_data='info')
b11 = InlineKeyboardButton(text='Да', callback_data='info')
b12 = InlineKeyboardButton(text='Нет', callback_data='main')
b2 = InlineKeyboardButton(text='Заказать', callback_data='call1')
bw = InlineKeyboardButton(text='Заказать', callback_data='call2')
be = InlineKeyboardButton(text='Заказать', callback_data='call3')
b3 = InlineKeyboardButton(text='Назад в меню', callback_data='back')
b4 = InlineKeyboardButton(text='Нет ',callback_data='register')
login = InlineKeyboardMarkup(resize_keyboard = True)\
    .add(login)
logreg = InlineKeyboardMarkup(resize_keyboard = True)\
    .add(login).add(b4)
zxc = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(asdh,asd2h)
zxc1 = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(asdh, asd5h)
zxc2 = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(asdh, asd12h)
zxc3 = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b1)
qweyhausmdj = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b11,b12)
qw7e8uh = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(bx1, b11)
a9iokjk = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(bq,bx)
asdjk = InlineKeyboardMarkup(resize_keyboard = True)\
    .row(ba)
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
    .add(b4).add(b11)
admin = InlineKeyboardMarkup(resize_keyboard=True)\
    .row(b1).add(b2, b0, b3, b4, b11)
sdj = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b0)
bnm = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(b4,bq1)