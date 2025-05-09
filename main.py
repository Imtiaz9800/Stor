import os
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    bot.start()
    bot.set_webhook(f"{WEBHOOK_URL}/{WEBHOOK_SECRET}")
