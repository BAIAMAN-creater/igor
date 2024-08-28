from database.models import *
import asyncio
import sys,logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.commands import router
from handlers.admin import admin_router
import yookassa

async def main():
    # await create_tables()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, admin_router)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# Напишите комманду phone которая отвечает дает номер телефона

# Напишите комманду id которая выводит id пользователя

























