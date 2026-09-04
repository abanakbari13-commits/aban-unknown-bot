import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = int(os.environ["ADMIN_ID"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 به Aban Unknown Bot خوش اومدی!\n\n"
        "پیامت رو همینجا بفرست تا به صورت ناشناس برای ادمین ارسال بشه."
    )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"شناسه عددی تلگرام شما:\n{update.effective_user.id}"
    )


async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message.text:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 پیام ناشناس:\n\n{message.text}"
        )

    elif message.photo:
        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=message.photo[-1].file_id,
            caption="📷 عکس ناشناس"
        )

    elif message.video:
        await context.bot.send_video(
            chat_id=ADMIN_ID,
            video=message.video.file_id,
            caption="🎥 ویدئوی ناشناس"
        )

    elif message.voice:
        await context.bot.send_voice(
            chat_id=ADMIN_ID,
            voice=message.voice.file_id,
            caption="🎤 پیام صوتی ناشناس"
        )

    elif message.document:
        await context.bot.send_document(
            chat_id=ADMIN_ID,
            document=message.document.file_id,
            caption="📎 فایل ناشناس"
        )

    else:
        await message.reply_text(
            "❌ این نوع پیام فعلاً پشتیبانی نمی‌شود."
        )
        return

    await message.reply_text(
        "✅ پیامت با موفقیت و به صورت ناشناس ارسال شد."
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))

    app.add_handler(
        MessageHandler(
            filters.ALL & ~filters.COMMAND,
            receive_message
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()
