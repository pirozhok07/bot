from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loguru import logger

start_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Показать товары'),
            KeyboardButton(text='Посмотреть корзину'),
            KeyboardButton(text='Мои заказы')
         ]
    ])


sub_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='cancel', callback_data='cancel')
         ]
    ])

def get_categories_kb(categories):
    category_menu = InlineKeyboardBuilder()
    i=0
    for category in categories:
        category_menu.row(InlineKeyboardButton(text=category[0], callback_data=f"category_{i}"))
        i+=1
    category_menu.add(InlineKeyboardButton(text='назад', callback_data=f"back"))
    return category_menu.as_markup()

def get_products_kb(products):
    products_menu = InlineKeyboardBuilder()
    i=0
    for product in products:
        products_menu.row(InlineKeyboardButton(text=f"{product[0]} {product[1]}", callback_data=f"product_{i}"))
        i+=1
    products_menu.add(InlineKeyboardButton(text='назад', callback_data=f"back"))
    return products_menu.as_markup()