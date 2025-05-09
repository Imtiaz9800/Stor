import os
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
from dotenv import load_dotenv
from handlers import start, earn, balance, buy_coin, batch_link, give_coin
from handlers.shortner import start_shortner, get_base_url, get_api_key, cancel, ASK_BASE_URL, ASK_API_KEY

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("earn", earn))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("buy_coin", buy_coin))
app.add_handler(CommandHandler("batch_link", batch_link))
app.add_handler(CommandHandler("give_coin", give_coin))

shortner_handler = ConversationHandler(
    entry_points=[CommandHandler("shortner", start_shortner)],
    states={
        ASK_BASE_URL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_base_url)],
        ASK_API_KEY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_api_key)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

app.add_handler(shortner_handler)

app.run_polling()