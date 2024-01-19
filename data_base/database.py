import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('super_roflo.db')
    cur = base.cursor()
    if base:
        print('Data base connected: OK')
    base.execute("CREATE TABLE IF NOT EXISTS list(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , adres TEXT, number TEXT)")
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT OR IGNORE INTO list(name, adres, number) VALUES(?, ?, ?)", tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM list').fetchall():
        await message.answer(f'Имя: {ret[1]}\nВаш адрес: {ret[2]}\nНомер телефона: {ret[3]}')

async def sql_read2():
    return cur.execute('SELECT * FROM list').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM list WHERE id == ?', (data,))
    base.commit()