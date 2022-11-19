from pyrogram import Client, idle
from config import *

AlphaAlone = Client(":alone:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Spl")))

AlphaAlone.start()
print("None")
idle()

