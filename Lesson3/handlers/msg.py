from aiogram import Router, types, F
from utils.random_fox import fox

router = Router()

@router.message(F.text.lower() == 'show fox')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Вот твоя лиса')
    await message.answer_photo(img_fox)
    img_fox = fox()
    await bot.send_photo(message.from_user.id, img_fox)