from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, CommandHandler, filters
from utils.admin import is_admin
import os

ASK_BASE_URL, ASK_API_KEY = range(2)

async def start_shortner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("You are not authorized to use this command.")
        return ConversationHandler.END

    await update.message.reply_text("Please send the base URL of the shortener.")
    return ASK_BASE_URL

async def get_base_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["base_url"] = update.message.text.strip()
    await update.message.reply_text("Now send the API key for this shortener.")
    return ASK_API_KEY

async def get_api_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api_key = update.message.text.strip()
    base_url = context.user_data["base_url"]

    shorteners = context.bot_data.get("shorteners", [])
    shorteners.append({"base_url": base_url, "api_key": api_key})
    context.bot_data["shorteners"] = shorteners

    await update.message.reply_text(f"Shortener added:
Base URL: {base_url}
API Key: {api_key}")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Shortener setup cancelled.")
    return ConversationHandler.END