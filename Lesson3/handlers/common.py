from aiogram import Router, types, F
from aiogram.filters.command import Command
from Lesson3.keyboards.keyboards import keyboard
from Lesson3.utils.random_fox import fox
import logging

router = Router()

@router.message(Command(commands="start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}",reply_markup=keyboard)

@router.message(Command(commands="стоп"))
@router.message(Command(commands="stop"))
async def stop(message: types.Message):
    #print(message.from_user.full_name)
    await message.answer(f"Пока, {message.from_user.full_name}")

@router.message(Command(commands="info"))
async def start(message: types.Message):
    await message.answer(f"Тестовый бот для проекта Нейрохищник на сайте GeekBrains")

#@dp.message(Command(commands=["info", 'инфо'])) пример перечисления слов активаторов команд
#@dp.message(F.text.lower() == 'инфо')
#async def info(message: types.Message):
    #   number = random.randint(0,100)
    #   await message.answer(f"Привет, твое число: {number}")

@router.message(F.text.lower() == 'show fox')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Вот твоя лиса')
    await message.answer_photo(img_fox)
    #img_fox = fox()
    #await bot.send_photo(message.from_user.id, img_fox)