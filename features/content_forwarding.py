import os
import redis
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# Redis setup
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Telegram Bot Token
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Expire messages at midnight
def get_ttl_for_midnight():
    now = datetime.now()
    midnight = now.replace(hour=23, minute=59, second=59, microsecond=0)
    return (midnight - now).seconds

# Expire messages after one week
def get_ttl_for_week():
    return 7 * 24 * 60 * 60  # 7 days in seconds

# Categorize and store posts
def categorize_and_store(message_text):
    today = datetime.now().strftime("%Y-%m-%d")
    ttl_midnight = get_ttl_for_midnight()

    if "#local" in message_text:
        redis_key = f"local_news:{today}"
        redis_client.rpush(redis_key, message_text)
        redis_client.expire(redis_key, ttl_midnight)
        print(f"Stored in {redis_key}: {message_text}")
    elif "#International" in message_text:
        redis_key = f"international_news:{today}"
        redis_client.rpush(redis_key, message_text)
        redis_client.expire(redis_key, ttl_midnight)
        print(f"Stored in {redis_key}: {message_text}")
    elif "#event" in message_text:
        ttl_week = get_ttl_for_week()  # TTL for events set to 1 week
        redis_key = f"events:{today}"
        redis_client.rpush(redis_key, message_text)
        redis_client.expire(redis_key, ttl_week)
        print(f"Stored in {redis_key}: {message_text}")
    elif "#internship" in message_text:
        ttl_week = get_ttl_for_week()  # TTL for events set to 1 week
        redis_key = f"internships:{today}"
        redis_client.rpush(redis_key, message_text)
        redis_client.expire(redis_key, ttl_week)
        print(f"Stored in {redis_key}: {message_text}")
    elif "#job" in message_text:
        ttl_week = get_ttl_for_week()  # TTL for events set to 1 week
        redis_key = f"jobs:{today}"
        redis_client.rpush(redis_key, message_text)
        redis_client.expire(redis_key, ttl_week)
        print(f"Stored in {redis_key}: {message_text}")
    elif "#humor" in message_text:
        ttl_week = get_ttl_for_week()  # TTL for events set to 1 week
        redis_key = f"humors:{today}"
        redis_client.rpush(redis_key, message_text)
        redis_client.expire(redis_key, ttl_week)
        print(f"Stored in {redis_key}: {message_text}")
    
    
    else:
        print("No matching category found for message.")


# Command: Start
async def daily_news_update(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Local News", callback_data="local_news")],
        [InlineKeyboardButton("International News", callback_data="international_news")],

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a category:", reply_markup=reply_markup)
async def tech_humor_update(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Humor", callback_data="humors")],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a category:", reply_markup=reply_markup)


async def tech_events_update(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Events", callback_data="events")],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a category:", reply_markup=reply_markup)

async def opportunities_menu(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Internships", callback_data="internships")],
        [InlineKeyboardButton("Jobs", callback_data="jobs")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a category:", reply_markup=reply_markup)


# Button Handler
# Button Handler
async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()

    category = query.data
    today = datetime.now().strftime("%Y-%m-%d")
    redis_key = f"{category}:{today}"

    messages = redis_client.lrange(redis_key, 0, -1)

    if messages:
        for message in messages:
            await query.message.reply_text(message)
    else:
        response = f"No {category.replace('_', ' ')} available for today."
        await query.edit_message_text(text=response)



# Listen for channel posts
async def handle_channel_post(update: Update, context):
    print(f"Update received: {update}")  # Debugging
    if update.channel_post:
        print(f"Post detected from channel: {update.channel_post.chat.username}")
        if update.channel_post.chat.username == CHANNEL_ID.replace("@", ""):
            message_text = update.channel_post.text
            if message_text:
                categorize_and_store(message_text)
            else:
                print("Post does not contain text.")
        else:
            print("Message received from a different channel.")



