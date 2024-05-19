from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='/info')

keyboard1 = [
    [button1, button2, button3],
    [button3, button1, button2]]

keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
