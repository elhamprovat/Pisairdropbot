import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# Load .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

# Gemini Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    prompt = f"""
Write a beautiful Telegram airdrop post.

User Link:
{user_text}

Rules:
- Attractive title
- Use emojis
- Keep it short
- Add hashtags
- Put the link at the end.
"""

    response = model.generate_content(prompt)

    await context.bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=response.text
    )

    await update.message.reply_text("✅ Posted Successfully!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot Started...")

app.run_polling()
