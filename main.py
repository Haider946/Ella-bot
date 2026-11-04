import os
import asyncio
import psycopg2
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '9233859229:AAHRFn-SJw_8MOf2Oyw4VrPi2l-EhAkRW8I'
DB_URL = '‎/postgres:tPzDrPEmr6hFkxlj@db.dffzchrqgxbzvvwjesef.supabase.co:5432/postgres'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Ella.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()
  
