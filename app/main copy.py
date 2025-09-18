import asyncio
import sys
import html

from loguru import logger

from aiogram import Bot, Dispatcher, types

import keyboards.user as kb

dp = Dispatcher()


# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     # await message.send_copy(chat_id=message.chat.id)
#     await message.answer("Я тебя люблю :3")

@dp.message()
async def start_handler(message: types.Message):
    # await repo.create_user(user_id=message.from_user.id)
    await message.answer(f'Hi, {html.escape(message.from_user.full_name)}',
                         reply_markup=kb.start_menu)
    


async def main() -> None:
    logger.add(sys.stderr, format="{time} {level} {message}", filter="template", level="INFO")
    
    logger.error("Starting bot")

    token = "8283170152:AAERIfVjJATqd2scCD5UVL7E2uwhjofdUdM"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())