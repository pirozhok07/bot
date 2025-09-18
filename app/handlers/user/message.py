import html

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from loguru import logger

import services.user as repo
import keyboards.user as kb

from crud import for_db

router = Router()
    
async def start_handler(message: Message):
    await repo.create_user(telegram_id=message.from_user.id, full_name=message.from_user.full_name, username=message.from_user.username)
    await message.answer(f'Hi, {html.escape(message.from_user.full_name)}, добро пожаловать в систему заказов.',
                         reply_markup=kb.start_menu)

async def show_category(message: Message):
    await for_db.check_table_products()
    await for_db.add_items_into_table_products()
    await message.answer("Категории:", reply_markup=kb.get_categories_kb(await for_db.get_categories()))
    
    logger.warning(await for_db.get_categories())

async def test(query: CallbackQuery):
    await query.message.edit_text(f'test 1')
    
async def test2(query: CallbackQuery):
    await query.message.edit_text(f'test 2')

async def send_echo(message: Message):
    await message.answer(text=message.text)

def register_handlers():
    router.message.register(start_handler, CommandStart())
    # router.message.register(show_product_handler, Command('show_product'))
    router.message.register(show_category, F.text == 'Показать товары')
    router.callback_query.register(test, Command('category_0'))
    router.callback_query.register(test2, F.text =='category_1')
    router.message.register(send_echo)