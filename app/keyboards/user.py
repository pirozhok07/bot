from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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

category_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='категория 1', callback_data='category_1'),
            InlineKeyboardButton(text='категория 2', callback_data='category_2'),
            InlineKeyboardButton(text='категория 3', callback_data='category_3')
          ]
    ])