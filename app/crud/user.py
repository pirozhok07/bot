from core.db import db
from loguru import logger

async def get_user(telegram_id: int):
    logger.error("telegram_id TRUE")
    return await db.fetchone('SELECT * FROM customers WHERE telegram_id = $1', (telegram_id,))


async def create_user(telegram_id: int, full_name: str, username:str):
    logger.error("telegram_id FALSE")
    return await db.execute('INSERT INTO customers (telegram_id, full_name, username) VALUES ($1, $2, $3)', (telegram_id, full_name, username,))
