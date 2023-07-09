import asyncio
from states.admin import comment
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text='/users')
async def admin_users(message: types.Message):
    f = open('chat_id.txt', 'r')
    text = f.read()
    txt = text.split(',')    
    f.close()    
    await message.answer(f"Bot statistikasi quyidagicha: \nBot lichkasidan foydalanayotganlar soni : {len(txt)-1} ta  ✅")

@dp.message_handler(text='/all_users')
async def admin_users(message: types.Message):
    f = open('users.txt', 'r')
    msg=''
    text1 = f.read()
    txt1 = text1.split(',')
    for i in range(0, len(txt1)-1):
        msg+=(f'{i+1}-foydalanuvchi @{txt1[i]}\n')
    f.close()    
    await message.answer(f"Bot statistikasi quyidagicha: \nBot lichkasidan foydalanayotganlar soni : {len(txt1)-1} ta  ✅\n{msg}")


@dp.message_handler(text='/reklama')
async def reklama(message: types.Message):
    f = open('chat_id.txt', 'r')
    text = f.read()
    txt = text.split(',')
    for i in range(0, len(txt)-1):
        chd = int(txt[i])
        f = open('reklama.txt', 'r')
        text = f.read()        
        f.close()     
        g = open('reklama_image.txt', 'r')
        photo_id = g.read()        
        g.close()   
        await bot.send_photo(
        chat_id=chd,
        photo=photo_id,
        caption=text,
        ) 
        await asyncio.sleep(0.05)
    f.close()       
    await  message.answer('Reklama jo`natildi.')

@dp.message_handler(text='admin', chat_id=5069753238)
async def reklama(message: types.Message):      
    await  message.answer(f'Admin panelga xush kelibsiz.\n/reklama - reklama textini hamma foydalanuvchilarga yuboradi.\n/reklama_edit - reklama textini o`zgartirish\n/users - Foydalanuvhcilar soni.\n/all_users - hamma foydalanuvchilar.\n@dars_jadval_bot_users - foydalanuvchilar haqidagi ma`lumot.')
   

@dp.message_handler(text='/reklama_edit')
async def reklama(message: types.Message):
    f = open('reklama.txt', 'r')
    text = f.read()        
    f.close()     
    g = open('reklama_image.txt', 'r')
    photo_id = g.read()        
    g.close()   
    await message.answer_photo(
        photo_id, caption=text
    )
    await  message.answer('Reklama textini jo`nating!')
    await comment.reklama_edit_text.set()

@dp.message_handler(state=comment.reklama_edit_text)
async def reklama(message: types.Message, state: FSMContext):
    f = open('reklama.txt', 'w')
    f.write(message.text)            
    await  message.answer('Reklama rasmini jo`nating!')
    await comment.reklama_edit_text.set()
    f.close()

@dp.message_handler(state=comment.reklama_edit_text, content_types=types.ContentType.PHOTO)
async def reklama(message: types.Message, state: FSMContext):
    f = open('reklama_image.txt', 'w')
    f.write(message.photo[-1].file_id)            
    await  message.answer('Reklama muvaffaqiyatli o`zgartirildi!')
    await state.finish()
    f.close()

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)



@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
