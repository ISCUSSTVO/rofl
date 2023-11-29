import sqlite3 as sq
from createbot import bot

def sql_start():
    global base, cur
    base = sq.connect('super_roflo.db')
    cur = base.cursor()
    if base:
        print('Data base connected: OK')
    base.execute('CREATE TABLE IF NOT EXISTS list(name TEXT PRIMARY KEY, adres TEXT, number INT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO list (name, adres, number) VALUES(?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM list').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[1]}\nИмя: {ret[2]}\nВаш адрес {ret[3]}\nНомер телефона')

async def sql_read2():
    return cur.execute('SELECT * FROM list').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM list WHERE name == ?', (data,))
    base.commit()