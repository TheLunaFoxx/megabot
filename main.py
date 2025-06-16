import asyncio
import os
from pyrogram import Client, filters, idle
from pyrogram.types import Message

# Print confirmation that the file is loading
print("🌟 Script has started loading")

# Load your environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create the bot client
app = Client("megabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private)
async def debug_handler(_, msg: Message):
    print(f"📩 PRIVATE MESSAGE: {msg.text} from {msg.from_user.id}")
    await msg.reply("✅ Bot received your message!")

async def main():
    await app.start()
    me = await app.get_me()
    print(f"🤖 Bot is running as @{me.username} (ID: {me.id})")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
