from telegram import Update
from telegram.ext import ContextTypes
from utils.shortener import shorten_url
from db import update_user_balance

async def earn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    long_url = "https://example.com/task"
    short_url = shorten_url(long_url)
    await update.message.reply_text(f"Click this link to earn 5 coins: {short_url}\nReply 'done' once completed.")

    def check_response(msg):
        return msg.from_user.id == user_id and msg.text.lower() == "done"

    msg = await context.application.bot.wait_for_message(timeout=300, check=check_response)
    if msg:
        update_user_balance(user_id, 5)
        await update.message.reply_text("You earned 5 coins!")