from Database.sisters import *
from Database.brothers import *
from Database.genders import *
from Spl import get_id
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

markup = IKM(
         [
         IKB(" ✅ ", callback_data="sibling_accept"),
         IKB(" ❌ ", callback_data="sibling_reject")
         ]
         )

s1_id = None
s2_id = None
s1_g = None
s2_g = None
s1_fn = None
s2_fn = None

@Client.on_message(filters.command("sibling", ["/", ".", "!", "?"]))
async def sibling(_, m):
    global s1_id
    global s2_id
    global s1_g
    global s2_g
    global s1_fn
    global s2_fn
    s1_id = m.from_user.id
    s2_id = await get_id(_, m) 
    s1_g = await check_gender(s1_id)
    s2_g = await check_gender(s2_id)
    s1_fn = (await _.get_users(s1_id)).first_name
    s2_fn = (await _.get_users(s2_id)).first_name
    if s2_g == "female":
        x = await is_sister(s1_id, s2_id)
        if x:
            return await m.reply("She is already your sister baka !")
        else:
            return await m.reply("{} wants {} as {} sister".format(s1_fn, s2_fn, "his" if s1_g=="male" else "her"), reply_markup=markup)
    else:
        x = await is_brother(s1_id, s2_id)
        if x:
            return await m.reply("He is already your brother baka !")
        else:
            return await m.reply("{} wants {} as {} brother".format(s1_fn, s2_fn, "his" if s1_g=="male" else "her"), reply_markup=markup)

@Client.on_callback_query(filters.regex("sibling_accept"))
async def sibling_cbq(_, q):
    global s1_id
    global s2_id
    global s1_g
    global s2_g
    global s1_fn
    global s2_fn
    if q.from_user.id != s2_id:
        return await q.answer("This is not for you baka !", show_alert=True)
    if s2_g == "female":
        await add_sister(s1_id, s2_id)
        if s1_g == "female":
            await add_sister(s2_id, s1_id)
        else:
            await add_brother(s2_id, s1_id)
    else:
        await add_brother(s1_id, s2_id)
        if s1_g == "female":
            await add_sister(s2_id, s1_id)
        else:
            await add_brother(s2_id, s1_id)
    await q.edit_message_text("{} accepted {} as {} {} !".format(s2_fn, s1_fn, "his" if s2_g=="male" else "her", "sister" if s1_g=="female" else "brother"))

@Client.on_callback_query(filters.regex("sibling_reject"))
async def rej(_, m):
    global s2_id
    if q.from_user.id != s2_id:
        return await q.answer("This is not for you baka !", show_alert=True)
    return await q.message.delete()

@Client.on_message(filters.command("leavesibling", ["/", ".", "?", "!"]))
async def leave(_, m):
    s1_id = m.from_user.id
    s2_id = await get_id(_, m)
    if s1_id == s2_id:
        return await m.reply("Baka !")
    s1_g = await check_gender(s1_id)
    s2_g = await check_gender(s2_id)
    if s2_g == "female":
        x = await is_sister(s1_id, s2_id)
        if not x:
            return await m.reply("She's not your sister baka !")
        else:
            await del_sister(s1_id, s2_id)
            if s1_g == "female":
                await del_sister(s2_id, s1_id)
            else:
                await del_brother(s2_id, s1_id)
            return await m.reply("Sister abandoned !")
    else:
        x = await is_brother(s1_id, s2_id)
        if not x:
            return await m.reply("He's not your brother baka !")
        else:
            await del_brother(s1_id, s2_id)
            if s1_g == "female":
                await del_sister(s2_id, s1_id)
            else:
                await del_brother(s2_id, s1_id)
            return await m.reply("Brother abandoned !")
