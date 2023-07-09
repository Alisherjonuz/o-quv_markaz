from aiogram import types
from keyboards.default.main import main
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer('Iltimos pastdagi tugmalardan foydalaning 👇', reply_markup = main)
