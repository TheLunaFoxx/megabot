import asyncio
import os
from pyrogram import Client, filters, idle
from pyrogram.types import Message

# Load from environment (Railway Variables)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("megabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_command(_, msg: Message):
    print(f"[DEBUG] Received /start from {msg.from_user.id}")
    await msg.reply_text("Hello! Your bot is fully working! ✅")

async def main():
    await app.start()
    me = await app.get_me()
    print(f"✅ Logged in as @{me.username} (ID: {me.id})")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
