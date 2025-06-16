import asyncio
import os
from pyrogram import Client, filters, idle
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

print("🌟 Script has loaded.")

app = Client("megabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private)
async def debug_all(_, msg: Message):
    print(f"[LOG] Incoming private message: {msg.text}")
    await msg.reply("🎯 The bot sees you!")

async def main():
    await app.start()
    me = await app.get_me()
    print(f"✅ Logged in as @{me.username} (ID: {me.id})")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
