from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

from config import BOT_TOKEN, CHANNEL_USERNAME
from ai import create_post


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    link = update.message.text.strip()

    # শুধু URL গ্রহণ করবে
    if not (link.startswith("http://") or link.startswith("https://")):
        await update.message.reply_text("❌ Please send a valid airdrop link.")
        return

    try:
        post = create_post(link)

        await context.bot.send_message(
            chat_id=CHANNEL_USERNAME,
            text=post,
            disable_web_page_preview=True
        )

        await update.message.reply_text("✅ Posted successfully!")

    except Exception as e:
        await update.message.reply_text(f"❌ Error:\n{e}")


def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("✅ Bot Started")
    app.run_polling()
