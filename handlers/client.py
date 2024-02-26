import sqlite3
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

import keyboard.client_kb
from createbot import dp, bot
from data_base import database
from keyboard import Regestration_kb
from keyboard import cjd

ID = None
save_id = 0

conn = sqlite3.connect('super_roflo.db')
cursor = conn.cursor()

moderator = ['krutoy_cell']

qwe = int(5000)
asd = int(3000)
zxc = int(2000)

class FSMRegestration(StatesGroup):
    custom_id = State()
    name = State()
    adres = State()
    number = State()
    rooms = State()
    new_adres = State()


@dp.callback_query_handler(text_contains=['main_win'])
async def main_win(call: CallbackQuery):
    await call.message.answer('Куда вы хотите заказать уборку', reply_markup=keyboard.client_kb.a9iokjk)

@dp.callback_query_handler(text_contains=['twink'])
async def new_adres(call: CallbackQuery, state: FSMContext):
    await FSMRegestration.new_adres.set()
    await call.message.answer('Введите новый адрес')

@dp.message_handler(state = FSMRegestration.new_adres)
async def load_new_adres(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_adres'] = message.text
    new_adres = data['new_adres']
    await message.answer(f' {new_adres}')
    await message.answer('Точно он?', reply_markup=keyboard.client_kb.qw7e8uh)
    await database.sql_add_command1(state)
    await state.finish()

@dp.message_handler(commands=['st'])
async def start(message: types.Message):
    await message.answer('/', reply_markup=keyboard.client_kb.sdj)

@dp.callback_query_handler(text_contains = ['register'], state=None)
async def start_registration(call: CallbackQuery):
    global ID
    await FSMRegestration.name.set()
    await call.message.answer('Введите ваше имя')

@dp.message_handler(state=FSMRegestration.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMRegestration.next()
    await message.answer('Теперь введите ваш адрес')

@dp.message_handler(state=FSMRegestration.adres)
async def load_adres(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adres'] = message.text
    await FSMRegestration.next()
    await message.answer('номер')

@dp.message_handler(state=FSMRegestration.number)
async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    await FSMRegestration.next()
    await message.answer('комнаты')


@dp.message_handler(state=FSMRegestration.rooms)
async def load_rooms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rooms'] = message.text
    name = data['name']
    number = data['number']
    room = data['rooms']
    await message.answer(f' {name}\n {number}\n {room}')
    await message.answer('Всё верно?', reply_markup=keyboard.client_kb.asdjk)
    await database.sql_add_command(state)
    await state.finish()

@dp.message_handler(commands='del')
async def delete_items(message: types.Message):
    read = await database.sql_read2()
    for ret in read:
        await bot.send_message(message.from_user.id, f'Каким зарегался: {ret[0]}\nИмя: {ret[1]}\nВаш адрес: {ret[2]}\nНомер телефона: {ret[3]}')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))

@dp.callback_query_handler(text_contains=['info'])
async def info(call: types.CallbackQuery):
    await call.message.answer('чё ты хочешь чмо', reply_markup=keyboard.cjd.asd)

@dp.callback_query_handler(text_contains=['dermo'])
async def dermo(call: CallbackQuery):
    await call.message.answer(f'иди нахер не готово ещё', reply_markup=keyboard.client_kb.zxc3)
@dp.callback_query_handler(text_contains='first')
async def wqe(call: CallbackQuery):
    await call.message.answer('чё то ещё?', reply_markup=keyboard.client_kb.zxc)
    await call.message.delete()

@dp.callback_query_handler(text_contains='second')
async def qwe(call: CallbackQuery):
    await call.message.answer('чё то ещё?', reply_markup=keyboard.client_kb.zxc1)
    await call.message.delete()

@dp.callback_query_handler(text_contains='third')
async def ewq(call: CallbackQuery):
    await call.message.answer('чё то ещё?', reply_markup=keyboard.client_kb.zxc2)
    await call.message.delete()

@dp.callback_query_handler(text_contains='call1')
async def call_service(call: CallbackQuery):
    await call.message.answer(f'\nhttps://sbp.nspk.ru/?ysclid=ls30ud2rj5955939254', reply_markup=keyboard.client_kb.superrofl)
    await call.message.delete()

@dp.callback_query_handler(text_contains='call2')
async def call_service1(call: CallbackQuery):
    await call.message.answer('\nhttps://sbp.nspk.ru/?ysclid=ls30ud2rj5955939254', reply_markup=keyboard.client_kb.superrofl)
    await call.message.delete()

@dp.callback_query_handler(text_contains='call3')
async def call_service2(call: CallbackQuery):
    await call.message.answer('плати пять тыща\nhttps://sbp.nspk.ru/?ysclid=ls30ud2rj5955939254', reply_markup=keyboard.client_kb.superrofl)
    await call.message.delete()



@dp.callback_query_handler(text_contains='back')
async def back(call: CallbackQuery):
    await call.message.answer('Выбери услугу', reply_markup=cjd.asd)
    await call.message.delete()

@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_querry: types.CallbackQuery):
    await database.sql_delete_command(callback_querry.data.replace('del ', ''))
    await callback_querry.answer(text=f'{callback_querry.data.replace("del ", "")} удалена.', show_alert=True)

@dp.message_handler(commands='del')
async def delete_items(message: types.Message):
    read = await database.sql_read2()
    for ret in read:
        await bot.send_message(message.from_user.id, f'Каким зарегался: {ret[0]}\nИмя: {ret[1]}\nВаш адрес: {ret[2]}\nНомер телефона: {ret[3]}')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(call_service, text_contains='7')
    dp.register_callback_query_handler(start_registration, text_contains='9')
    dp.register_callback_query_handler(call_service, text_contains='call')
    dp.register_callback_query_handler(call_service1, text_contains='call1')
    dp.register_callback_query_handler(call_service2, text_contains='call2')
    dp.register_callback_query_handler(back, text_contains='back')
    dp.register_message_handler(load_name, state=FSMRegestration.name)
    dp.register_message_handler(load_adres, state=FSMRegestration.adres)
    dp.register_message_handler(load_number, state=FSMRegestration.number)
    dp.message_handler(cancel_handler, state="*", commands='отмена')
    dp.message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")