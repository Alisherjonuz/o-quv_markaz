from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard = [
            [
                KeyboardButton(text="ℹ️ Biz haqimizda ℹ️"),
                KeyboardButton(text="Suhbatga yozilish"),
            ],            
        ],
        resize_keyboard=True
)

