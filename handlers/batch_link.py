from telegram import Update
from telegram.ext import ContextTypes

async def batch_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please upload up to 20 files. This feature will store them and generate a unique batch link.")