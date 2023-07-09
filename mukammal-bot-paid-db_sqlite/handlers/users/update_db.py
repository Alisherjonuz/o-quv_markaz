from aiogram import types
from sre_parse import State
from aiogram.dispatcher import FSMContext
from keyboards.default.subject import subject
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message, ReplyKeyboardRemove
from states.register import register
from loader import dp, db, bot

alisherjon = -1001703158141

@dp.message_handler(text = "Suhbatga yozilish")
async def register_1(message: types.Message, state: FSMContext):
    await message.answer(f"👤 Iltimos ism, familiyangizni yozing 👤 \nMasalan: Numonov Alisher")
    await register.name.set()

@dp.message_handler(state = register.name)
async def bot_start(message: types.Message, state: FSMContext):
    name = message.text
    db.update_user_name(name=name, id=message.from_user.id)
    await message.answer(f"📞 Telefon raqamingizni yuboring 📞\nMasalan: +99891 234 56 78")
    await register.phone.set()


@dp.message_handler(state = register.phone)
async def bot_start(message: types.Message, state: FSMContext):
    phone = message.text
    db.update_user_phone(phone=phone, id=message.from_user.id)
    await message.answer(f"🏠 Manzilingizni yuboring 🏠\nMasalan: Toshkent shahar Chilonzor tuman")
    await register.address.set()


@dp.message_handler(state = register.address)
async def bot_start(message: types.Message, state: FSMContext):
    address = message.text
    db.update_user_address(address=address, id=message.from_user.id)
    await message.answer(f"📚 Fanni tanlang 📚", reply_markup=subject)
    await register.subject.set()

@dp.message_handler(state = register.subject)
async def bot_start(message: types.Message, state: FSMContext):
    subject = message.text
    db.update_user_subject(subject=subject, id=message.from_user.id)
    msg = db.select_user(id = message.from_user.id)
    al = msg[1]+msg[2]+msg[3]+msg[4]
    await bot.send_message(chat_id=alisherjon, text=al)

    await message.answer(f"Ma\'lumotlaringiz saqlandi")
    await state.finish()
