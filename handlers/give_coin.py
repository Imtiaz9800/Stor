from telegram import Update
from telegram.ext import ContextTypes
from db import update_user_balance
from utils.admin import is_admin

async def give_coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("You are not authorized to use this command.")
        return

    try:
        user_id = int(context.args[0])
        coins = int(context.args[1])
        update_user_balance(user_id, coins)
        await update.message.reply_text(f"Gave {coins} coins to user {user_id}.")
    except:
        await update.message.reply_text("Usage: /give_coin <user_id> <coins>")