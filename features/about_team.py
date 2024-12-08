import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Team member details with direct Google Drive image links
team_members = {
    "about_ruth": {"name": "Ruth Dehne", "role": "Designer", "image": "https://drive.google.com/uc?id=1iHlui8Jg_nxtHrlqjq8J6SiEER19RsCK"},
    "about_tolosa": {"name": "Tolosa Diriba", "role": "Marketing Lead", "image": "https://drive.google.com/uc?id=1mVtUn7-iXSysMzw423jlVTBtlLn1T_TZ"},
    "about_duresa": {"name": "Duresa Guye", "role": "Developer & SEO Optimizer", "image": "https://drive.google.com/uc?id=1X3nWqUE73Zj1qF8ij2hNlNAFiVxmXf7v"},
    "about_muhamed": {"name": "Muhamed Ahmed", "role": "Video Editor", "image": "https://drive.google.com/uc?id=1VW-8slHZrGjYqEaqu8GXyXMClViQPKC7"},
    "about_hilina": {"name": "Hilina Adane", "role": "Content Creator & Writer", "image": "https://drive.google.com/uc?id=1RISH8WX0nnlpmuBeHuqFLX9sPT03KNyj"},
    "about_alpha": {"name": "Alpha Lencho", "role": "Social Media Manager", "image": "https://drive.google.com/uc?id=1l8O-4Vd3Gnqqm9kA3GLun2Cl_02SvSqy"},
}



# About Team handler
async def about_team(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Meet the Team:\n\n"
    for member in team_members.values():
        image_url = member["image"]
        await update.message.reply_photo(
            photo=image_url,
            caption=f"{member['name']} - {member['role']}",
        )

# Function to handle the callback for individual team members
async def about_individual_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    team_member = team_members.get(update.message.text.lower().replace(" ", "_"))
    if team_member:
        await update.message.reply_photo(
            photo=team_member["image"],
            caption=f"{team_member['name']} - {team_member['role']}",
        )

# Main function to set up the bot
def main():
    # Create the Application with the bot's token
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Text("About Techኢት"), about_team))
    application.add_handler(MessageHandler(filters.Text("About the Team"), about_team))
    
    # Add individual team member handlers
    for member in team_members:
        application.add_handler(MessageHandler(filters.Text(f"About {team_members[member]['name']}"), about_individual_member))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
