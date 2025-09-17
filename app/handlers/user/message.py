import html

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import services.user as repo
import keyboards.user as kb

from crud import for_db

router = Router()
    
async def start_handler(message: Message):
    await repo.create_user(telegram_id=message.from_user.id, full_name=message.from_user.full_name, username=message.from_user.username)
    await message.answer(f'Hi, {html.escape(message.from_user.full_name)}, добро пожаловать в систему заказов.',
                         reply_markup=kb.start_menu)
    
async def show_goods_handler(message: Message):
    await message.answer('Категории', reply_markup=kb.category_menu)

async def show_category(message: Message):
    await for_db.add_items_into_table_products()
    await message.answer(for_db.get_categories())

def register_handlers():
    router.message.register(start_handler, CommandStart())
    # router.message.register(show_product_handler, Command('show_product'))
    router.message.register(show_goods_handler, F.text == 'Показать товары')
    router.message.register(show_category, F.text == '/cat')