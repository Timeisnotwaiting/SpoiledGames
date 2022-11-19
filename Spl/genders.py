from Database.genders import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

id = None

@Client.on_message(filters.command("gender"))
async def gender(_, m):
    global id
    id = m.from_user.id
    x = await check_gender(id)
    y = "Male 👦" if x == "male" else "Female 👧"
    markup = IKM(
         [
         [
         IKB(" {} ".format(y), callback_data="gender_toggle")
         ]
         ]
         )
    await m.reply("Your status !", reply_markup=markup)

@Client.on_callback_query(filters.regex("gender_toggle") & filters.user(id))
async def gend(_, q):
    await change_gender(q.from_user.id)
    x = await check_gender(id)
    y = "Male 👦" if x == "male" else "Female 👧"
    markup = IKM(
         [
         [
         IKB(" {} ".format(y), callback_data="gender_toggle")
         ]
         ]
         )
    await q.edit_message.reply_markup(reply_markup=markup)



    
