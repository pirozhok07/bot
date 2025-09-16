import html

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import keyboards.user as kb

router = Router()

async def start_handler(message: Message):
    # await repo.create_user(user_id=message.from_user.id)
    await message.answer(f'Hi, {html.escape(message.from_user.full_name)}',
                         reply_markup=kb.start_menu)
    
def register_handlers():
    router.message.register(start_handler, CommandStart())