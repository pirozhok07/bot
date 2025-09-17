from core.db import db

async def add_user_table(user_id: int):
    return await db.execute('''
            CREATE TABLE IF NOT EXISTS customers(
                       customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       telegram_id INTEGER UNIQUE NOT NULL,
                       full_name TEXT,
                       username TEXT,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                       ''')

async def get_user(telegram_id: int):
    return await db.fetchone('SELECT * FROM customers WHERE telegram_id = $1', (telegram_id,))


async def create_user(telegram_id: int, full_name: str, username:str):
    return await db.execute('INSERT INTO customers (telegram_id, full_name, username) VALUES ($1, $2, $3)', (telegram_id, full_name, username,))
