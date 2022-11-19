from Database.brothers import brothersdb
from pyrogram import Client, filters

@Client.on_message(filters.command("del"))
async def dele(_, m):
    b1_id = int(m.text.split()[1])
    try:
        await brothersdb.delete_one({"b1_id": b1_id})
        await m.reply("deleted")
    except Exception as e:
        print(e)
        await m.reply(e)
