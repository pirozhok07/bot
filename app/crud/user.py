import db


async def get_user(user_id: int):
    return await db.fetchone('SELECT * FROM users WHERE user_id = $1', (user_id,))


async def create_user(user_id: int, full_name: str, username:str):
    return await db.execute('INSERT INTO users (user_id, full_name, username) VALUES ($1, $2, $3)', (user_id, full_name, username,))
