import html

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import keyboards.user as kb

router = Router()

async def start_handler(message: Message):
    # await repo.create_user(user_id=message.from_user.id)
    await message.answer(f'Hi, {html.escape(message.from_user.full_name)}, добро пожаловать в систему заказов.',
                         reply_markup=kb.start_menu)
    
async def show_product_handler(message: Message):
    await message.answer('Категории', reply_markup=kb.category_menu)


def register_handlers():
    router.message.register(start_handler, CommandStart())
    router.message.register(show_product_handler, Command('show_product'))
    # router.message.register(menu_handler, F.text == 'menu')