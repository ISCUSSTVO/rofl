import sqlite3
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import keyboard.client_kb
from createbot import dp, bot
from data_base import database
from keyboard import Regestration_kb
from keyboard import cjd

conn = sqlite3.connect('super_roflo.db')
cursor = conn.cursor()

ID = None

class FSMRegestration(StatesGroup):
    name = State()
    adres = State()
    number = State()

class FSMClient(StatesGroup):
    name2 = State()

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    await bot.send_message(message.from_user.id, 'Здарова', reply_markup=Regestration_kb.button_case_regestration)
    await message.delete()

@dp.message_handler(commands=['Лист'])
async def list(message: types.Message):
    await database.sql_read(message)

@dp.message_handler(commands='Заказ_услуги', state=None)
async def call_service(message: types.Message):
    if message.from_user.id == ID:
        await message.answer('Выбери услугу', reply_markup=cjd.asd)
        await message.delete()
    else:
        await message.answer('Иди зарегайся')

@dp.message_handler(commands=['Информация_об_услугах'], state=None)
async def info_service(message: types.Message):
    if message.from_user.id == ID:
        await message.answer('Выберите услугу по которой хотите получить информацию', reply_markup=cjd.asd)
        await message.delete()
    else:
        await message.answer('Иди зарегайся')

@dp.message_handler(commands='Регестрация', state=None)
async def cm_start(message: types.Message):
    await FSMRegestration.name.set()
    await message.reply('Введи своё имя')

@dp.message_handler(state=FSMRegestration.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMRegestration.next()
    await message.reply('Теперь введи свой адрес')
@dp.message_handler(content_types=['adres'], state=FSMRegestration.adres)
async def load_adres(message: types.Message, state: FSMContext):
    async with state.proxy()as data:
        data['adres'] = message.text
    await FSMRegestration.next()
    await message.reply('Тепрь введи свой номер телефона')
@dp.message_handler(content_types=['number'], state=FSMRegestration.number)
async def load_number(message: types.Message, state: FSMContext):
    global ID
    ID = message.from_user.id
    async with state.proxy() as data:
        data['number'] = message.text
    await database.sql_add_command(state)
    await state.finish()

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

@dp.message_handler(commands='Удалить')
async def delete_items(message: types.Message):
    read = await database.sql_read2()
    for ret in read:
        await bot.send_message(message.from_user.id, f'Имя: {ret[0]}\nВаш адрес: {ret[1]}\nНомер телефона: {ret[2]}')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))

@dp.message_handler(commands=['client'])
async def client(message: types.Message):
    if message.from_user.id == ID:
        await message.reply('Что нужно', reply_markup=keyboard.client_kb.prikol)
    else:
        await message.answer('Ди зарегайся')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(client, commands=['client'])
    dp.register_message_handler(call_service, commands=['Заказ_услуги'])
    dp.register_message_handler(info_service, commands=['Информация_об_услугах'])
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cm_start, commands=['Регестрация'], state=None)
    dp.register_message_handler(list, commands=['Лист'])
    dp.register_message_handler(load_name, state=FSMRegestration.name)
    dp.register_message_handler(load_adres, state=FSMRegestration.adres)
    dp.register_message_handler(load_number, state=FSMRegestration.number)
    dp.message_handler(cancel_handler, state="*", commands='отмена')
    dp.message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")


