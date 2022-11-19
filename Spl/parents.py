from Database.parents import *
from Database.kids import *
from Database.genders import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

k_id = None
p_id = None
kid_g = None
parent_g = None
k_fn = None
p_fn = None

@Client.on_message(filters.command("parent", ["/", "?", "!", "."]))
async def parents_add(_, m):
    global k_id
    global p_id
    global kid_g
    global parent_g
    global k_fn
    global p_fn
    k_id = m.from_user.id
    if m.reply_to_message:
        p_id = m.reply_to_message.from_user.id
    else:
        txt = m.text.split()
        if txt[1][0] == "@":
            p_id = (await _.get_users(txt[1])).id
        else:
            p_id = int(txt[1])
    kid_g = await check_gender(k_id)
    parent_g = await check_gender(p_id)
    x = await is_parent(k_id, p_id)
    if x:
        return await m.reply("{} is already your parent !".format("She" if parent_g == "female" else "He"))
    kids = await get_kids(p_id)
    if len(kids) == 5:
        return await m.reply("Maximum number of kids reached !")
    parents = await get_parents(k_id)
    if len(parents) == 2:
        return await m.reply("Maximum number of parents reached !")
    markup = IKM(
             [
             IKB(" ✅ ", callback_data=parent_accept),
             IKB(" ❌ ", callback_data=parent_reject)
             ]
             )
    k_fn = m.from_user.first_name
    p_fn = (await _.get_users(p_id)).first_name
    await _.send_message(m.chat.id, "{} wants {} as {} {}".format(k_fn, p_fn, "his" if kid_g == "male" else "her", "Dad" if parent_g == "male" else "Mom"), reply_markup=markup)

@Client.on_callback_query(filters.regex("parent_accept"))
async def acc(_, q):
    global k_id
    global p_id
    global kid_g
    global parent_g
    global k_fn
    global p_fn
    if q.from_user.id != p_id:
        return await q.answer("This is not for you baka !", show_alert=True)
    await add_parent(k_id, p_id)
    await add_kid(p_id, k_id)
    return await q.edit_message_text("{} accepted {} as {} {}".format(p_fn, k_fn, "his" if parent_g=="male" else "her", "Son" if kid_g=="male" else "Daughter"))

@Client.on_callback_query(filters.regex("parent_reject"))
async def rej(_, m):
    global p_id
    if q.from_user.id != p_id:
        return await q.answer("This is not for you baka !", show_alert=True)
    return await q.message.delete()


@Client.on_message(filters.command("leaveparent", ["/", ".", "?", "!"]))
async def leaveparent(_, m):
    k_id = m.from_user.id
    if m.reply_to_message:
        p_id = m.reply_to_message.from_user.id
    else:
        txt = m.text.split()
        if txt[1][0] == "@":
            p_id = (await _.get_users(txt[1])).id
        else:
            p_id = int(txt[1])
    x = await is_parent(k_id, p_id)
    parent_g = await check_gender(p_id)
    if not x:
        return await m.reply("{} is not your parent baka !".format("He" if parent_g=="male" else "She"))
    await del_parent(k_id, p_id)
    await del_kid(p_id, k_id)
    await m.reply("parent abandoned !")
