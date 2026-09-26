import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "សូមស្វាគមន៍មកកាន់ SB24 Lucky - ស្ដេច​បក្សី។\n"
        "ទទួលបានព័ត៌មាន និងការជូនដំណឹងថ្មីៗតាម Telegram។"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "SB24 Lucky - ស្ដេច​បក្សី\n"
        "ព័ត៌មាន និងការជូនដំណឹងថ្មីៗពី SB24 Lucky។"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bot is online and ready.")


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
