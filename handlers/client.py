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

previous_messages = {}

class FSMRegestration(StatesGroup):
    custom_id = State()
    name = State()
    adres = State()
    number = State()

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    await message.answer('Здарова', reply_markup=Regestration_kb.button_case_regestration)
    await message.delete()

@dp.callback_query_handler(text_contains='register', state=None)
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
    await message.answer('Теперь введите ваш номер телефона')

@dp.message_handler(state=FSMRegestration.number)
async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    await message.answer('Регестрация завершена')
    name = data['name']
    number = data['number']
    adres = data['adres']
    await message.answer(f'{name}\n{adres}\n{number}')

    await message.answer('Всё верно?', reply_markup=keyboard.client_kb.superultrarofl)
    await database.sql_add_command(state)
    await state.finish()

@dp.message_handler(commands='del')
async def delete_items(message: types.Message):
    read = await database.sql_read2()
    for ret in read:
        await bot.send_message(message.from_user.id, f'Каким зарегался: {ret[0]}\nИмя: {ret[1]}\nВаш адрес: {ret[2]}\nНомер телефона: {ret[3]}')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))

@dp.message_handler(commands=['list'])
async def list(message: types.Message):
    await database.sql_read(message)


@dp.callback_query_handler(text_contains='info')
async def call_service(call: CallbackQuery):
    await call.message.answer('Выбери услугу', reply_markup=cjd.asd)
    await call.message.delete()

@dp.callback_query_handler(text_contains='first')
async def call_service(call: CallbackQuery):
    await call.message.answer('чето там чето там', reply_markup=keyboard.client_kb.rofl)
    await call.message.delete()

@dp.callback_query_handler(text_contains='second')
async def call_service(call: CallbackQuery):
    await call.message.answer('бла бла бла', reply_markup=keyboard.client_kb.rofl)
    await call.message.delete()

@dp.callback_query_handler(text_contains='third')
async def call_service(call: CallbackQuery):
    await call.message.answer('ещё одна параша', reply_markup=keyboard.client_kb.rofl)
    await call.message.delete()

@dp.callback_query_handler(text_contains='call')
async def call_service(call: CallbackQuery):
    await call.message.answer('Заказал, молодец, теперь выйди', reply_markup=keyboard.client_kb.superrofl)
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

@dp.message_handler(commands=['client'])
async def client(message: types.Message):
    if message.from_user.username in moderator:
        await message.answer('че надо', reply_markup=keyboard.client_kb.admin)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(client, commands=['client'])
    dp.register_callback_query_handler(call_service, text_contains='7')
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_callback_query_handler(start_registration, text_contains='9')
    dp.register_callback_query_handler(call_service, text_contains='call')
    dp.register_callback_query_handler(back, text_contains='back')
    dp.register_message_handler(list, commands=['list'])
    dp.register_message_handler(load_name, state=FSMRegestration.name)
    dp.register_message_handler(load_adres, state=FSMRegestration.adres)
    dp.register_message_handler(load_number, state=FSMRegestration.number)
    dp.message_handler(cancel_handler, state="*", commands='отмена')
    dp.message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")