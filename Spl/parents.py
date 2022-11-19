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

    
