from telegram import Update
from telegram.ext import ContextTypes

async def buy_coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To buy coins, contact the admin.")