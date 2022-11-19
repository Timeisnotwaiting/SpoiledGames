from Database.parents import parentsdb
from pyrogram import Client, filters

@Client.on_message(filters.command("del"))
async def dele(_, m):
    k_id = int(m.text.split()[1])
    try:
        await parentsdb.delete_one({"k_id": k_id})
        await m.reply("deleted")
    except Exception as e:
        print(e)
        await m.reply(e)
