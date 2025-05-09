from telegram import Update
from telegram.ext import ContextTypes
from db import get_user

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    await update.message.reply_text(f"You have {user.get('coins', 0)} coins.")