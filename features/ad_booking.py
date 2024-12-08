from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, InputFile
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ApplicationBuilder,
    ContextTypes,
    filters
)
import logging

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Price dictionary for the packages
packages = {
    "12_hours": "150 Birr",
    "24_hours": "200 Birr",
    "3_days": "490 Birr",
    "5_days": "590 Birr",
    "7_days": "790 Birr"
}

# Admins' chat IDs (replace with actual chat IDs)
admins = [6927234281, 691090883, 112233445, 998877665, 556677889, 223344556]  # Replace with actual chat IDs

# Function to start the bot and show the main menu
async def ad_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat.id
    logger.info(f"Chat ID: {chat_id}")
    keyboard = [
        ["12 hours", "24 hours"],
        ["3 days", "5 days"],
        ["7 days", "Back to Main Menu"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        """🎉 Welcome to Ad Booking! 🎉

🚀 Daily Packages:

✨ Half a Day: Just 150 Birr for 12 hours of prime advertising!
🌟 Full Day: Get the spotlight all day long for only 200 Birr (24 hours)!
💼 Weekly Packages:

🔥 3 Days: Boost your visibility for 490 Birr!
🔥 5 Days: Maximize your reach for only 590 Birr!
🔥 7 Days: Go all-in and make an impact for just 790 Birr!

📅 Choose your perfect package:
            """,
        reply_markup=reply_markup
    )

# Function to handle the ad booking after a user selects a package
async def select_package(update: Update, context: ContextTypes.DEFAULT_TYPE):
    package_choice = update.message.text.strip().lower().replace(" ", "_")
    
    logger.info(f"User selected: {update.message.text} (Processed: {package_choice})")

    if package_choice in packages:
        confirm_keyboard = [
            [KeyboardButton("Yes, confirm")],
            [KeyboardButton("No, cancel")],
            [KeyboardButton("Back to Main Menu")]
        ]
        reply_markup = ReplyKeyboardMarkup(confirm_keyboard, resize_keyboard=True)
        await update.message.reply_text(
            f"You selected the {package_choice.replace('_', ' ').title()} package for {packages[package_choice]}. Is that correct?",
            reply_markup=reply_markup
        )
        context.user_data["package_choice"] = package_choice
    else:
        await update.message.reply_text(
            "Invalid package selection. Please choose one of the following: 12 hours, 24 hours, 3 days, 5 days, 7 days."
        )
        await ad_booking(update, context)

# Function to handle the user's confirmation or cancellation
async def handle_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    response = update.message.text.strip().lower()

    if "package_choice" in user_data:
        package_choice = user_data["package_choice"]

        if response == "yes, confirm":
            price = packages.get(package_choice)
            await update.message.reply_text(
                f"Your ad has been booked for {package_choice.replace('_', ' ').title()} at {price}. Please upload a screenshot of your payment.",
                reply_markup=ReplyKeyboardMarkup([["Back to Main Menu"]], resize_keyboard=True)
            )
        elif response == "no, cancel":
            await update.message.reply_text(
                "Booking process has been canceled. You can start again anytime.",
                reply_markup=ReplyKeyboardMarkup([["Back to Main Menu"]], resize_keyboard=True)
            )
            context.user_data.clear()
        else:
            await update.message.reply_text(
                "Invalid response. Please choose 'Yes, confirm', 'No, cancel', or 'Back to Main Menu'."
            )
    else:
        await update.message.reply_text("It seems you haven't booked an ad yet. Please start the booking process first.")

# Function to handle photo upload
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    if "package_choice" in user_data:
        package_choice = user_data["package_choice"]
        price = packages.get(package_choice)

        await update.message.reply_text(
            f"Thank you for your upload! We will process your booking for the {package_choice.replace('_', ' ').title()} package at {price} shortly.",
            reply_markup=ReplyKeyboardMarkup([["Back to Main Menu"]], resize_keyboard=True)
        )

        # Notify admins
        photo_file = update.message.photo[-1]
        photo_id = photo_file.file_id

        for admin in admins:
            try:
                await context.bot.send_photo(
                    chat_id=admin,
                    photo=photo_id,
                    caption=f"New ad booking!\n\nPackage: {package_choice.replace('_', ' ').title()}\nPrice: {price}\nUser: @{update.message.from_user.username or 'Unknown User'}"
                )
            except Exception as e:
                logger.error(f"Error sending photo to admin {admin}: {e}")

        context.user_data.clear()
    else:
        await update.message.reply_text("It seems you haven't booked an ad yet. Please start the booking process first.")

# Function to handle cancellation
async def cancel_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Your booking has been canceled. You can start again whenever you want.",
        reply_markup=ReplyKeyboardMarkup([["Back to Main Menu"]], resize_keyboard=True)
    )
    context.user_data.clear()
