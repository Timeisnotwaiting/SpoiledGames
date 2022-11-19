from Database.parents del_parent
from pyrogram import Client, filters

@Client.on_message(filters.command("del"))
async def del(_, m):
    query1 = int(m.text.split()[1])
    query2 = int(m.text.split()[2])
    try:
        await del_parent(query1, query2)
        await m.reply("deleted")
    except Exception as e:
        await m.reply(e)
