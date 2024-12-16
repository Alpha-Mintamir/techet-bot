#!/usr/bin/env python
# pylint: disable=unused-argument

# I advise not touching the first line.


from telegram.ext import  CallbackQueryHandler
from features.content_forwarding import *
from features.about_team import *
from features.about_techet import *
from features.services import *
from features.podcast import *
from  features.ad_booking import *

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    raise ValueError("BOT_TOKEN and CHANNEL_ID must be set in the .env file.")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling /start command")
    keyboard = [
        ["Daily News", "Podcast"],
        ["Opportunities", "Our Service"],
        ["Ad Booking", "About Us"],
        ["Tech Humor", "Tech Events"],

    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to Techet Bot! Choose a segment below:",
        reply_markup=reply_markup,
    )



async def podcast_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Podcast menu")
    keyboard = [
        ["Season 1", "Season 2", "Season 3"],
        ["Back to Main Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to the Podcast section. Choose a season below:",
        reply_markup=reply_markup,
    )


async def season1_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Season 1 menu")
    keyboard = [
        ["E01", "E02", "E03", "E04", "E05"],
        ["E06", "E07", "E08", "E09", "E10"],
        ["E11", "E12", "E13", "E14"],
        ["Back to Season Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Choose an episode below:",
        reply_markup=reply_markup,
    )



async def season2_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Season 2 menu")
    keyboard = [
        ["S02E01", "S02E02", "S02E03", "S02E04", "S02E05"],
        ["S02E06", "S02E07", "S02E08", "S02E09", "S02E10"],
        ["S02E11", "S02E12", "S02E13", "S02E14"],
        ["Back to Season Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Choose an episode below:",
        reply_markup=reply_markup,
    )



async def season3_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Season 3 menu")
    keyboard = [
        ["S03E01"],
        ["Back to Season Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Choose an episode below:",
        reply_markup=reply_markup,
    )


# Function to handle the "season 3" menu
async def add_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Season 3 menu")
    keyboard = [
        ["12 hours", "24 hours", "3 days"],
        ["5 days", "7 days"],
        ["Back to Main Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Choose an episode below:",
        reply_markup=reply_markup,
    )


# Function to handle the "About Us" menu
async def about_us_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling About Us menu")
    keyboard = [
        ["About Techኢት", "About the Team"],
        ["Back to Main Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Explore the About Us section:", reply_markup=reply_markup
    )



async def our_service_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Our Service menu")
    keyboard = [
        ["🎁 Package One", "🎁 Package Two", "🎁 Package Three"],
        ["Back to Main Menu"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        """The Social Media Management Gap
Many businesses struggle to manage their social media effectively, often due to a lack of time, expertise, or resources. Consistent content creation, engagement, and performance tracking can be overwhelming, leading to missed opportunities for growth and brand visibility.

At Techኢት, we bridge this gap by offering professional social media management services. We take care of everything from content creation and design to engagement and performance analysis, ensuring your social media presence is active, engaging, and aligned with your business goals. Let us handle your social media while you focus on growing your business.
        Explore our Social Media Management Packages:""", reply_markup=reply_markup
    )


# Function to handle the "Back to Main Menu" button
async def back_to_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Back to Main Menu button")
    await start(update, context)


# Function to handle the "Back to Season Menu" button
async def back_to_season_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Back to Season Menu button")
    await podcast_menu(update, context)



if __name__ == "__main__":

    app = ApplicationBuilder().token(BOT_TOKEN).build()


    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text("Daily News"), daily_news_update))
    app.add_handler(MessageHandler(filters.Text("Tech Events"), tech_events_update))
    app.add_handler(MessageHandler(filters.Text("Tech Humor"), tech_humor_update))
    app.add_handler(MessageHandler(filters.Text("Podcast"), podcast_menu))
    app.add_handler(MessageHandler(filters.Text("About Us"), about_us_menu))
    app.add_handler(MessageHandler(filters.Text("Our Service"), our_service_menu))
    app.add_handler(MessageHandler(filters.Text("Opportunities"), opportunities_menu))
    app.add_handler(MessageHandler(filters.Text("Season 1"), season1_menu))
    app.add_handler(MessageHandler(filters.Text("Season 2"), season2_menu))
    app.add_handler(MessageHandler(filters.Text("Season 3"), season3_menu))
    app.add_handler(MessageHandler(filters.Text("Back to Main Menu"), back_to_main_menu))
    app.add_handler(MessageHandler(filters.Text("Back to Season Menu"), back_to_season_menu))
    app.add_handler(MessageHandler(filters.Text("Ad Booking"), ad_booking))

    app.add_handler(MessageHandler(filters.Text("About Techኢት"), about_techet))
    app.add_handler(MessageHandler(filters.Text("About the Team"), about_team))

    app.add_handler(MessageHandler(filters.Text("🎁 Package One"), package_one))
    app.add_handler(MessageHandler(filters.Text("🎁 Package Two"), package_two))
    app.add_handler(MessageHandler(filters.Text("🎁 Package Three"), package_three))

    app.add_handler(MessageHandler(filters.Regex("^(12 hours|24 hours|3 days|5 days|7 days)$"), select_package))
    app.add_handler(MessageHandler(filters.Regex("^(Yes, confirm|No, cancel|Back to Main Menu)$"), handle_confirmation))

    app.add_handler(CommandHandler('cancel', cancel_booking))

    # Add individual team member handlers
    for member_key in team_members:
        app.add_handler(
            MessageHandler(filters.Text(f"About {team_members[member_key]['name']}"), about_individual_member))

    app.add_handler(MessageHandler(filters.Text("E01"), episode_e01))
    app.add_handler(MessageHandler(filters.Text("E02"), episode_e02))
    app.add_handler(MessageHandler(filters.Text("E03"), episode_e03))
    app.add_handler(MessageHandler(filters.Text("E04"), episode_e04))
    app.add_handler(MessageHandler(filters.Text("E05"), episode_e05))
    app.add_handler(MessageHandler(filters.Text("E06"), episode_e06))
    app.add_handler(MessageHandler(filters.Text("E07"), episode_e07))
    app.add_handler(MessageHandler(filters.Text("E08"), episode_e08))
    app.add_handler(MessageHandler(filters.Text("E09"), episode_e09))
    app.add_handler(MessageHandler(filters.Text("E10"), episode_e10))
    app.add_handler(MessageHandler(filters.Text("E11"), episode_e11))
    app.add_handler(MessageHandler(filters.Text("E12"), episode_e12))
    app.add_handler(MessageHandler(filters.Text("E13"), episode_e13))
    app.add_handler(MessageHandler(filters.Text("E14"), episode_e14))

    app.add_handler(MessageHandler(filters.Text("S02E01"), episode_e16))
    app.add_handler(MessageHandler(filters.Text("S02E02"), episode_e17))
    app.add_handler(MessageHandler(filters.Text("S02E03"), episode_e18))
    app.add_handler(MessageHandler(filters.Text("S02E04"), episode_e19))
    app.add_handler(MessageHandler(filters.Text("S02E05"), episode_e20))
    app.add_handler(MessageHandler(filters.Text("S02E06"), episode_e21))
    app.add_handler(MessageHandler(filters.Text("S02E07"), episode_e22))
    app.add_handler(MessageHandler(filters.Text("S02E08"), episode_e23))
    app.add_handler(MessageHandler(filters.Text("S02E09"), episode_e24))
    app.add_handler(MessageHandler(filters.Text("S02E10"), episode_e25))
    app.add_handler(MessageHandler(filters.Text("S02E11"), episode_e26))
    app.add_handler(MessageHandler(filters.Text("S02E12"), episode_e27))
    app.add_handler(MessageHandler(filters.Text("S02E13"), episode_e28))
    app.add_handler(MessageHandler(filters.Text("S02E14"), episode_e29))
    app.add_handler(MessageHandler(filters.Text("S03E01"), episode_e30))
    

    
    

    app.add_handler(CallbackQueryHandler(button_handler))

    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, handle_message))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_transaction_number))

    app.run_polling(allowed_updates=Update.ALL_TYPES)