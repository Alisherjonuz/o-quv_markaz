import sqlite3
import logging
from data.config import CHANNELS
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import main
from keyboards.inline.subscription import check_button
from data.config import ADMINS
from loader import dp, db, bot


alisherjon = -1001703158141

@dp.message_handler(text='/start')
async def show_channels(message: types.Message):
    # await bot.send_message(alisherjon, f"Yangi foydalanuvchi\nUsername: {message.from_user.username}\nChat id: {message.from_user.chat_id}\nFirst name: {message.from_user.first_name}")
    
    f = open('chat_id.txt', 'r')
    text = f.read().split(',')
    id = f'{message.from_user.id}'
    alisher = 0
    for i in text:
        if i == id:
            alisher += 1
    f.close()
    if alisher == 0:
        f = open('chat_id.txt', 'a')
        f.write(f'{message.from_user.id},')
        f.close()
        await bot.send_message(
            chat_id=alisherjon, text=f"Yangi foydalanuvchi!\nUsername: @{message.from_user.username}\nChat id: {message.from_user.id}\nFirst name: {message.from_user.first_name}"
        )

    f = open('users.txt', 'r')
    text = f.read().split(',')
    username = message.from_user.username
    alisher = 0
    for i in text:
        if i == username:
            alisher += 1
    f.close()
    if alisher == 0:
        f = open('users.txt', 'a')
        f.write(f'{message.from_user.username},')
        f.close()

    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
    await message.answer(f"Salom, {message.from_user.first_name}! Botimizga xush kelibsiz")
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id)
    except sqlite3.IntegrityError as err:
        await message.answer(text='Iltimos pastdagi tugmalardan birini tanlang ', reply_markup=main)


    # Adminga xabar beramiz
  

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f" ✅✅✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f" ❌❌❌ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)


