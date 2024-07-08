from loader import bot, dp, db
from models.btm import BotUser, Group
from aiogram import types
from keyboards.inline.simplein import add_to_group
from keyboards.default.simple import admin_panel_keys, uzbekistan_regions_uz
from aiogram.types import ReplyKeyboardRemove

ADMINS = [756639030, 5138942987]


@dp.message_handler(state="*", commands=['start'])
async def start_command(message: types.Message):
    if message.chat.type == 'private':
        if message.chat.id in ADMINS:
            await bot.send_message(
                message.chat.id,
                text="Admin Panel",
                reply_markup=admin_panel_keys
            )
        else:
            if db.query(BotUser).filter(BotUser.telegram_id == message.from_user.id).scalar() is None:
                db.add(BotUser(telegram_id=message.from_user.id, name=message.from_user.first_name if message.from_user.first_name else '' + ' ' + message.from_user.last_name if message.from_user.last_name else ''))
                db.commit()
            await bot.send_message(
                message.chat.id,
                text=f"✅ Kanal va Guruhlarga yuborilgan so'rovlarni avtomatik tarzda qabul qiluvchi bot!\nBot ishlashi uchun kanalga qo'shib admin qilishingiz kerak 👇",
                reply_markup=add_to_group
            )
    elif message.chat.type == 'group' or message.chat.type == 'supergroup' and message.from_user.id in ADMINS:
        user = await bot.get_chat_member(message.chat.id, bot.id)
        chat_id = message.chat.id
        in_db = db.query(Group).filter(Group.telegram_id == message.chat.id).scalar()
        if in_db is None:
            db.add(Group(telegram_id=chat_id, title=message.chat.title))
            db.commit()
        if user.status == 'administrator' or user.status == 'creator':
            await bot.send_message(chat_id, "<b>✅ Bot o'z faoliyatini boshladi!</b>", parse_mode="HTML")
        else:
            await bot.send_message(chat_id, "<b>🙅‍♂️ Botga administrator huquqini berishingiz lozim!</b>", parse_mode="HTML")



@dp.message_handler(state="*", content_types=['text'])
async def text_handle(message: types.Message):
    if message.chat.type == 'private':
        if message.text in uzbekistan_regions_uz:
            await bot.send_message(
                message.chat.id,
                text="<b>Ma'lumot saqlandi!</b>",
                reply_markup=ReplyKeyboardRemove(),
                parse_mode='HTML'
            )
            
            
@dp.message_handler(state="*", commands=['statistics_user_admin'])
async def statistics_admin(message: types.Message):
    users = db.query(BotUser).all()
    text = '1.'
    for i in users:
        text+=f"{i.name} - {i.telegram_id}"
    print('assaki')
    await bot.send_message(
                message.chat.id,
                text=f"{text}",
            )
