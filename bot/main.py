import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_BOT_TOKEN = "7899174821:AAFQptWye0nSsxBdOdl6HMfJrtPfYlUTCqQ"  # Replace this
OLLAMA_URL = 'http://ollama:11434/api/generate'  # container-to-container hostname
MODEL = 'llama3'  # or 'llama2', 'gemma', etc.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Hello! I'm your local LLM bot. Ask me anything.")

def query_ollama(prompt):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })
        return response.json().get("response", "⚠️ No response.")
    except Exception as e:
        logger.error(f"Ollama error: {e}")
        return "⚠️ Failed to reach AI backend."

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply = query_ollama(user_input)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("🤖 Bot running...")
    app.run_polling()

if __name__ == '__main__':
    main()
