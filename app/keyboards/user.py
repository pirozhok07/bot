from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
    for category in categories:
        category_menu.add(InlineKeyboardButton(text=category, callback_data=f"category_{category}"))
    category_menu.as_markup()