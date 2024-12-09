import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Updated team member details with descriptions, roles, and LinkedIn links
team_members = {
    "about_duresa": {
        "name": "Duresa Guye",
        "role": "SEO Specialist & Full-Stack Developer",
        "description": (
            "Responsible for driving the overall business strategy, enhancing online presence through"
            "effective SEO practices, and developing comprehensive digital solutions from front-end to "
            "back-end to ensure seamless user experiences and functionality."
        ),
        "link": "https://www.linkedin.com/in/duresa-guye-5aba5625a/",
        "image": "https://drive.google.com/uc?id=1uNM71cNWHz4w6VvC38paEhVlrLCcvTEa"

,
    },
    "about_alpha": {
        "name": "Alpha Lencho",
        "role": "Social Media Manager & AI and ML Engineer",
        "description": (
            "Responsible for managing social media strategies, creating engaging content, and fostering a strong "
            "online presence while also developing and deploying machine learning models and AI-driven solutions "
            "to optimize processes and enhance user experience."
        ),
        "link": "https://www.linkedin.com/in/alpha-lencho-13b8281bb/",
        "image": "https://drive.google.com/uc?id=1l8O-4Vd3Gnqqm9kA3GLun2Cl_02SvSqy",
    },
    "about_hilina": {
        "name": "Hilina Adane",
        "role": "Content Creator & Copyright Specialist",
        "description": (
            "Responsible for creating engaging content across multiple platforms" 
        ),
        "link": "https://www.linkedin.com/in/hilina-adane-524494228/",
"image": "https://drive.google.com/uc?id=1dlyzzgl-DTX_1RJ4cm13V3h-zwAD-Hqi"
    },
    "about_ruth": {
        "name": "Ruth Dehene",
        "role": "UX/UI & Graphics Designer",
        "description": (
            "Responsible for designing user-centric interfaces that provide seamless, intuitive experiences while "
            "crafting visually appealing graphics to enhance brand identity and user engagement across digital platforms."
        ),
        "link": "https://www.linkedin.com/in/ruth-dehene-404373318/",
        "image": "https://drive.google.com/uc?id=1iHlui8Jg_nxtHrlqjq8J6SiEER19RsCK",
    },
    "about_tolosa": {
        "name": "Tolosa Diriba",
        "role": "Video Editor, Web Developer & Digital Marketing Specialist",
        "description": (
            "Responsible for transforming raw footage into engaging, high-quality videos, developing and maintaining websites "
            "with a focus on functionality and user experience, and implementing digital marketing strategies to boost online "
            "presence and drive audience engagement."
        ),
        "link": "https://www.linkedin.com/in/tolosa-diriba-95624a286/",
        "image": "https://drive.google.com/uc?id=1mVtUn7-iXSysMzw423jlVTBtlLn1T_TZ",
    },
    "about_muhammed": {
        "name": "Muhammed Ahmed",
        "role": "Video Editor and Security Analyst",
        "description": (
            "Responsible for editing and producing high-quality videos to effectively communicate messages, while ensuring the "
            "security and integrity of digital assets and systems by analyzing vulnerabilities, implementing protective measures, "
            "and maintaining secure online environments."
        ),
        "link": "https://www.linkedin.com/in/muhammed-ahmed",
        "image": "https://drive.google.com/uc?id=1qK41Wtc5442JePUqWGOE9mccm8ON5YKm"

,
    },
}

# About Team handler
async def about_team(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Meet the Team:\n\n"
    for member in team_members.values():
        await update.message.reply_photo(
            photo=member["image"],
            caption=f"{member['name']} - {member['role']}\n\n{member['description']}\n\nLinkedIn: {member['link']}",
        )

# Function to handle the callback for individual team members
async def about_individual_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    team_member = team_members.get(update.message.text.lower().replace(" ", "_"))
    if team_member:
        await update.message.reply_photo(
            photo=team_member["image"],
            caption=f"{team_member['name']} - {team_member['role']}\n\n{team_member['description']}\n\nLinkedIn: {team_member['link']}",
        )