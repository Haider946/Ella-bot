import os
import asyncio
import psycopg2
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 'YOUR_TELEGRAM_TOKEN'
DB_URL = 'YOUR_POSTGRES_URL'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Ella. I'm fully awake now.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm working on my advanced logic! Ask me something else later.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    print("Bot is running...")
    app.run_polling()
  
