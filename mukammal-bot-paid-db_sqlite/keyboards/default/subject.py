from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


subject = ReplyKeyboardMarkup(
    keyboard = [
            [
                KeyboardButton(text="📌Tarix"),
                KeyboardButton(text="📌Fizika"),
            ],      
            [
                KeyboardButton(text="📌Rus tili"),
                KeyboardButton(text="📌Ona tili"),
            ],  
            [
                KeyboardButton(text="📌Matematika"),
                KeyboardButton(text="📌Mental Arifmetika"),
            ],  
            [
                KeyboardButton(text="📌Ingiliz tili"),
                KeyboardButton(text="📌Dasturlash"),
            ],        
            [
                KeyboardButton(text="📌Prezident maktablariga tayyorlash"),
                KeyboardButton(text="🔙 Orqaga 🔙"),
            ],  
        ],
        resize_keyboard=True
)

