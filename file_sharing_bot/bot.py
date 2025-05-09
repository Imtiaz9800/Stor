from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from utils.database import initialize_user, update_coins
from utils.shortener import shorten_url
from utils.coin_system import deduct_coins
import config

# Initialize the bot
bot = Bot(token=config.TG_BOT_TOKEN)
updater = Updater(token=config.TG_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Start command handler
def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    initialize_user(user_id)
    update.message.reply_text(config.START_MESSAGE)

# Command to give coins to a user (admin only)
def give_coins(update: Update, context: CallbackContext):
    if update.message.from_user.id not in config.ADMINS:
        update.message.reply_text("You are not authorized to use this command.")
        return
    try:
        user_id = int(context.args[0])
        coins = int(context.args[1])
        update_coins(user_id, coins)
        update.message.reply_text(f"Successfully added {coins} coins to user {user_id}.")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /give_coins <user_id> <coins>")

# Add more command handlers as needed
# ...

# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('give_coins', give_coins))

# Start the bot
updater.start_polling()
updater.idle()

