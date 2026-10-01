import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]


def sports_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("⚽ ការប្រកួតបន្តផ្ទាល់", callback_data="live"),
            InlineKeyboardButton("📅 ការប្រកួតនាពេលខាងមុខ", callback_data="upcoming"),
        ],
        [
            InlineKeyboardButton("🏆 លទ្ធផលថ្មីៗ", callback_data="results"),
            InlineKeyboardButton("🌍 ពានរង្វាន់ និងលីគ", callback_data="leagues"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "⚽ សូមស្វាគមន៍មកកាន់ SB24 Live Info!\n\n"
        "ទទួលបានព័ត៌មានអំពីការប្រកួតកីឡា លទ្ធផល "
        "និងព័ត៌មានកីឡាថ្មីៗតាម Telegram។\n\n"
        "សូមជ្រើសរើសព័ត៌មានដែលអ្នកចង់មើល៖",
        reply_markup=sports_menu(),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    messages = {
        "live": (
            "⚽ ការប្រកួតបន្តផ្ទាល់\n\n"
            "សូមរង់ចាំព័ត៌មានការប្រកួតបន្តផ្ទាល់ថ្មីៗ។"
        ),
        "upcoming": (
            "📅 ការប្រកួតនាពេលខាងមុខ\n\n"
            "ព័ត៌មានអំពីការប្រកួតនាពេលខាងមុខនឹងបង្ហាញនៅទីនេះ។"
        ),
        "results": (
            "🏆 លទ្ធផលថ្មីៗ\n\n"
            "លទ្ធផលការប្រកួតថ្មីៗនឹងបង្ហាញនៅទីនេះ។"
        ),
        "leagues": (
            "🌍 ពានរង្វាន់ និងលីគ\n\n"
            "ព័ត៌មានអំពីពានរង្វាន់ និងលីគកីឡានឹងបង្ហាញនៅទីនេះ។"
        ),
    }

    await query.message.reply_text(
        messages.get(query.data, "សូមជ្រើសរើសជម្រើសមួយ។"),
        reply_markup=sports_menu(),
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "SB24 Live Info\n"
        "ព័ត៌មានអំពីការប្រកួតកីឡា លទ្ធផល និងព័ត៌មានថ្មីៗអំពីកីឡាតាម Telegram។"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bot is online and ready.")


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
