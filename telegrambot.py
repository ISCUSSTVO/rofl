from aiogram import executor
from createbot import dp
from data_base import database
from handlers import client
async def on_startup(_):
    print("Бот вышел в онлайн")
    database.sql_start()

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)