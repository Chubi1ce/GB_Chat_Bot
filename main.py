import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

#Логирование
logging.basicConfig(level=logging.INFO)

#Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(Command(commands="start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}")

@dp.message(Command(commands="стоп"))
@dp.message(Command(commands="stop"))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f"Пока, {message.from_user.full_name}")

@dp.message(Command(commands="info"))
async def start(message: types.Message):
    await message.answer(f"Тестовый бот для проекта Нейрохищник на сайте GeekBrains")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())