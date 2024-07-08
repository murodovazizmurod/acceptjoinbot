from aiogram import types
from keyboards.inline.simplein import add_to_group
from keyboards.default.simple import select_region
from loader import dp, bot, db
from models.btm import BotUser



@dp.chat_join_request_handler()
async def chat_join(message: types.ChatJoinRequest):
    try:
        await message.approve()
    except Exception as e:
        print(e)
        await bot.send_message(756639030, f"{e}")
    try:
        if db.query(BotUser).filter(BotUser.telegram_id == message.from_user.id).scalar() is None:
            db.add(BotUser(telegram_id=message.from_user.id, name=message.from_user.first_name if message.from_user.first_name else '' + ' ' + message.from_user.last_name if message.from_user.last_name else ''))
            db.commit()
        await bot.send_message(message.user_chat_id, f'<b>✅ Tabriklaymiz siz "{message.chat.title}" kanalga a\'zo bo\'ldingiz! Barcha ma\'lumotlarni kanalda ko\'rishingiz mumkin!</b>', reply_markup=add_to_group, parse_mode="HTML")
        await bot.send_message(message.user_chat_id, '<b>Siz qaysi viloyatdansiz?</b>', reply_markup=select_region, parse_mode="HTML")
    except Exception as e:
        print(e)
        await bot.send_message(756639030, f"{e}")