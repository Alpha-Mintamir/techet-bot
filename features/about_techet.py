from telegram import Update
from telegram.ext import ContextTypes


async def about_techet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    about_text = (
        "Welcome to Techኢት, your premier destination for all things technology!\n\n"
        "Our mission is to provide a comprehensive platform where tech enthusiasts, "
        "professionals, and beginners alike can come together to explore, learn, "
        "and stay updated with the latest trends in the tech world.\n\n"
        "At Techኢት, we believe that technology is the driving force behind innovation and progress. "
        "Through our insightful blogs and engaging podcasts, we aim to inspire and educate "
        "our community by sharing valuable knowledge, expert opinions, and industry news.\n\n"
        "Thank you for being a part of the Techኢት community!"
    )
    await update.message.reply_text(about_text)
