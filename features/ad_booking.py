from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
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

# Function to start the bot and show the main menu
async def ad_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("12 hours", callback_data="twelve_hours")],
        [InlineKeyboardButton("24 hours", callback_data="twenty_four_hours")],
        [InlineKeyboardButton("3 days", callback_data="three_days")],
        [InlineKeyboardButton("5 days", callback_data="five_days")],
        [InlineKeyboardButton("7 days", callback_data="seven_days")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to Ad Booking! Choose your package:",
        reply_markup=reply_markup
    )

# Function to show pricing and handle booking based on selection
async def button_ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    package_choice = query.data
    price = packages.get(package_choice, None)

    if price:
        message = f"You have selected {package_choice.replace('_', ' ').title()}.\nThe price is {price}."
        keyboard = [
            [InlineKeyboardButton("Book Now", callback_data=f"book_{package_choice}")],
            [InlineKeyboardButton("Cancel", callback_data="cancel_booking")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=message, reply_markup=reply_markup)
    else:
        await query.edit_message_text(text="Invalid selection. Please try again.")

# Function to handle booking confirmation
async def book_ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    package_choice = query.data.replace("book_", "")
    price = packages.get(package_choice, None)

    if price:
        # Notify admin about the booking
        await context.bot.send_message(
            chat_id="@alphityy",
            text=f"New ad booking! Package: {package_choice.replace('_', ' ').title()}, Price: {price}."
        )

        # Ask the user to upload the screenshot of the transaction
        await query.edit_message_text(
            text=f"Your ad has been booked for {package_choice.replace('_', ' ').title()} at {price}.\nPlease upload a screenshot of your money transfer."
        )

        # Store user's choice in context.user_data for later processing
        context.user_data["package_choice"] = package_choice
        context.user_data["price"] = price

# Function to handle the screenshot upload
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    if "package_choice" in user_data:
        await update.message.reply_text(
            f"Thank you for your upload! We will process your ad booking shortly. Package: {user_data['package_choice'].replace('_', ' ').title()}."
        )

        # Optionally, send a confirmation to the user
        await update.message.reply_text("Your ad booking is confirmed. Stay tuned for your ad to be posted!")

        # Clear the user data
        context.user_data.clear()
    else:
        await update.message.reply_text("It seems you haven't booked an ad yet. Please start the booking process first.")

# Function to handle cancellation
async def cancel_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Your booking has been canceled. You can start again whenever you want.")