from Database.parents import del_parent
from pyrogram import Client, filters

@Client.on_message(filters.command("del"))
async def dele(_, m):
    query1 = int(m.text.split()[1])
    query2 = int(m.text.split()[2])
    try:
        await del_parent(query1, query2)
        await m.reply("deleted")
    except Exception as e:
        print(e)
        await m.reply(e)
