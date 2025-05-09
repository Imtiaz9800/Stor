from telegram import Update
from telegram.ext import ContextTypes
from db import get_or_create_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    get_or_create_user(user_id)
    await update.message.reply_text("Welcome! Use /earn to earn coins and /balance to check your coins.")