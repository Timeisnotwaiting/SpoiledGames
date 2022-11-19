from Database.sisters import *
from Database.brothers import *
from Database.genders import *
from Spl import get_id

markup = IKM(
         [
         IKB(" ✅ ", callback_data="sibling_accept"),
         IKB(" ❌ ", callback_data="sibling_reject")
         ]
         )

@Client.on_message(filters.command("sibling"))
async def sibling(_, m):
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
