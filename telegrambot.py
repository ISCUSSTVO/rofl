from aiogram import executor
from createbot import dp
from data_base import database
async def on_startup(_):
    print("Бот вышел в онлайн")
    database.sql_start()

from handlers import client
client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)