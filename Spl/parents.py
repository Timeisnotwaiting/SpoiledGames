from Database.parents import *
from Database.kids import *
from Database.genders import *
from pyrogram import Client, filters

@Client.on_message(filters.command("parent", ["/", "?", "!", "."]))
async def parents_add(_, m):
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
    if x:
        return await m.reply("
