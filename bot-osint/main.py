import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from osint.ip_lookup import lookup_ip
from osint.email_lookup import lookup_email

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def osint_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Format: /osint_email <email>")
        return

    email = context.args[0]
    result = lookup_email(email)
    await update.message.reply_text(result, parse_mode="Markdown")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 OSINT Bot Siap!\nGunakan /osint_ip <IP> untuk mulai.")

async def osint_ip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Format: /osint_ip <alamat IP>")
        return

    ip = context.args[0]
    result = lookup_ip(ip)
    await update.message.reply_text(result)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("osint_ip", osint_ip))
    app.add_handler(CommandHandler("osint_email", osint_email))
    print("Bot berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()

