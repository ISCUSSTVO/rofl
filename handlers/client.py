from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from createbot import dp, bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboard import client_kb
from keyboard import cjd
from data_base import database
from keyboard import Regestration_kb
x = int(0)
y = int(0)
z = int(0)

bool(x)
bool(y)
bool(z)

class FSMClient(StatesGroup):
    name = State()
    adres = State()
    number = State()
x = 1

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    await bot.send_message(message.from_user.id, 'Здарова', reply_markup=Regestration_kb.button_case_regestration)
    await message.delete()

@dp.message_handler(commands=['list'])
async def list(message: types.Message):
    await database.sql_read(message)

@dp.message_handler(commands='Заказ_услуги', state=None)
async def call_service(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выбери услугу', reply_markup=cjd.asd)
    await message.delete()

@dp.message_handler(commands=['Информация_об_услугах'], state=None)
async def info_service(message: types.Message):
    await message.reply('Выберите услугу по которой хотите получить информацию', reply_markup=cjd.asd)
    await message.delete()

@dp.message_handler(commands='Регестрация', state=None)
async def cm_start(message: types.Message):
    await FSMClient.name.set()
    await message.reply('Введи своё имя')

@dp.message_handler(state=FSMClient.name)
async def load_name(message: types.Message, state: FSMContext):
    not bool(x)
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.reply('Теперь введи свой адрес')
@dp.message_handler(content_types=['adres'], state=FSMClient.adres)
async def load_adres(message: types.Message, state: FSMContext):
    not bool(y)
    async with state.proxy()as data:
        data['adres'] = message.text
    await FSMClient.next()
    await message.reply('Тепрь введи свой номер телефона')
@dp.message_handler(content_types=['number'], state=FSMClient.number)
async def load_number(message: types.Message, state: FSMContext):
    not bool(z)
    async with state.proxy() as data:
        data['number'] = float(message.text)

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
        await bot.send_message(message.from_user.id, f'{ret[0]}\nИмя {ret[1]}\nАдрес {ret[2]}\nНомер')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))

@dp.message_handler(commands=['client'])
async def client(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберете, что вам нужно', reply_markup=client_kb.prikol)
    await message.delete()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(client, commands=['client'])
    dp.register_message_handler(call_service, commands=['Заказ_услуги'])
    dp.register_message_handler(info_service, commands=['Информация_об_услугах'])
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cm_start, commands=['Регестрация'], state=None)
    dp.register_message_handler(list, commands=['list'])
    dp.register_message_handler(load_name, state=FSMClient.name)
    dp.register_message_handler(load_adres, state=FSMClient.adres)
    dp.register_message_handler(load_number, state=FSMClient.number)
    dp.message_handler(cancel_handler, state="*", commands='отмена')
    dp.message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")


