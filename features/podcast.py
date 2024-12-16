from telegram import Update
from telegram.ext import ContextTypes

# Placeholder logger
import logging
logger = logging.getLogger(__name__)

# Define episode functions
async def episode_e01(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E01")
    await update.message.reply_photo(
        photo="https://i1.rgstatic.net/ii/profile.image/11431281182142399-1692301882182_Q512/Dereje-Teferi.jpg",
        caption=(
            "🎙️ **Guest Name:** Dr. Dereje Teferi\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/dereje-teferi/)\n"
            "📖 *Description:* Head of School of Information Science.\n"
            "▶️ [Watch on YouTube](https://youtu.be/kE7QLONzSFE)"
        ),
        parse_mode="Markdown",
    )

async def episode_e02(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E02")
    await update.message.reply_photo(
        photo="https://media.istockphoto.com/id/1290743328/vector/faceless-man-abstract-silhouette-of-person-the-figure-of-man-without-a-face-front-view.jpg?s=612x612&w=0&k=20&c=Ys-4Co9NaWFFBDjmvDJABB2BPePxJwHugC8_G5u0rOk=",
        caption=(
            "🎙️ **Guest Name:** Andargachew Asfaw\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/andargachew-asfaw/)\n"
            "📖 *Description:* Lecturer at Addis Ababa University School of Information Science.\n"
            "▶️ [Watch on YouTube](https://youtu.be/LvVEU67Bcgs)"
        ),
        parse_mode="Markdown",
    )
async def episode_e03(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E03")
    
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQGsji8khdrBBQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1725878281158?e=1738800000&v=beta&t=v-B7jXx0eTyCe0cQ_Zoih9emwy4NeOvsSUa7iI5xxyw",
        caption=(
            "🎙️ **Guest Name:** Abenezer Seifu\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/abenezer-seifu/)\n"
            "📖 *Description:* Software Engineering Student at AAiT.\n"
            "▶️ [Watch on YouTube Part 1](https://youtu.be/xSE0TtkZszM?si=5By51qdKTsHTvV2b)"
            "▶️ [Watch on YouTube Part 2](https://youtu.be/reEm4kzKYFo?si=c8R-DgGQGoBIRAmA)"
            "▶️ [Watch on YouTube Part 3](https://youtu.be/h7mg_Jp11Y0?si=VCgt7JlwSLn8VDnU)"
        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQHSKppnZup7cg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1728915978854?e=1738800000&v=beta&t=Re63BwuN61zm2d0G2hDm3VYY9IVqaWib7LMJ4aQ7nv4",
        caption=(
            "🎙️ **Guest Name:** Abdulaziz Zeinu\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/abzaek/)\n"
            "📖 *Description:* Software Engineering Student at AAiT.\n"
            "▶️ [Watch on YouTube Part 1](https://youtu.be/xSE0TtkZszM?si=5By51qdKTsHTvV2b)"
            "▶️ [Watch on YouTube Part 2](https://youtu.be/reEm4kzKYFo?si=c8R-DgGQGoBIRAmA)"
            "▶️ [Watch on YouTube Part 3](https://youtu.be/h7mg_Jp11Y0?si=VCgt7JlwSLn8VDnU)"
        ),
        parse_mode="Markdown",
    )


async def episode_e04(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E03")
    
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFxph_Za9pkmQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1729414174125?e=1739404800&v=beta&t=gIIhlpen1K8WeYAE7delOHjFvbNkD_9kLdgQ1XQv9ak",
        caption=(
            "🎙️ **Guest Name:** Dawit Sishu\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/dawitsishu/)\n"
            "📖 *Description:* Information Systems Graduate | Co-founder oc ICC.\n"
            "▶️ [Listen on Telegram](https://t.me/TechInEthio/508)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQHGo7FcfFPK_w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1721247596158?e=1739404800&v=beta&t=pKCAaMPmPthF4AUycWnmMsRhwhA6CRqCJ5r26QEPsQ8",
        caption=(
            "🎙️ **Guest Name:** Zelalem Yohannes\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/zelalemyohannes/)\n"
            "📖 *Description:* Information Systems Graduate | Co-founder oc ICC.\n"
            "▶️ [Listen on Telegram](https://t.me/TechInEthio/508)"

        ),
        parse_mode="Markdown",
    )

async def episode_e08(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E05")
    
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQHJUVZ-1dr62Q/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1699677373718?e=1740009600&v=beta&t=5ogdkVq6fadm3ZjJ9Dc3nMKY0WB0GfXMkjBa-cdJ7nU",
        caption=(
            "🎙️ **Guest Name:** Fuad Muhammad\n"
            "🔗 [LinkedIn Profile]https://www.linkedin.com/in/fuadmuhe/)\n"
            "📖 *Description:* Software Engineering Student at AAiT.\n"
            "▶️ [Watch on YouTube Part 1](https://youtu.be/UqgqNtKpuGI?si=bHEgAeiri8mcKluW)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFu2iksDaPTMA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1690223096149?e=1740009600&v=beta&t=CA6L22Vc1awfPkXtuUWKyMgoK_iZjsHz6DhgAaPKmuE",
        caption=(
            "🎙️ **Guest Name:** Bisrat Asaye\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/bisrat-asaye/)\n"
            "📖 *Description:* Software Engineering Student at AAiT.\n"
            "▶️ [Watch on YouTube Part 1](https://youtu.be/UqgqNtKpuGI?si=bHEgAeiri8mcKluW)"

        ),
        parse_mode="Markdown",
    )

async def episode_e06(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E06")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQHSaWD6bMUATw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1725706669746?e=1740009600&v=beta&t=1du6dM_eL80BwPekUMBNakF0S6s5f6SNVefwZOxd4tk",
        caption=(
            "🎙️ **Guest Name:**  Mulu Tsega\n"
            "🔗 [LinkedIn Profile](https://et.linkedin.com/in/mulu-tsega943)\n"
            "📖 *Description:* Product Manager.\n"
            "▶️ [Watch on YouTube](https://youtu.be/Crfy2QkeM0M?si=KbgjBrOmbdC4AiTT)"
        ),
        parse_mode="Markdown",
    )

async def episode_e07(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E07")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQENfKntCISt6w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1730144167795?e=1740009600&v=beta&t=3cTbEUa05Twyk3YDYN6Ot6R0i-66_EFmWMxVxCFhZ-o",
        caption=(
            "🎙️ **Guest Name:** Samrawit Dawit\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/samrawit-dawit-59a5b4250/)\n"
            "📖 *Description:* Emma is a software engineer specializing in cloud computing.\n"
            "▶️ [Watch on YouTube](https://www.youtube.com/watch?v=88bENK06E2c)"
        ),
        parse_mode="Markdown",
    )

async def episode_e05(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E08")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D5603AQEu5f3_eY4M-A/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1725288544229?e=1740009600&v=beta&t=Qi_BKHXNtmu-ofYUq5_XxpfFtHvGDlDGdyDD0qfJgcM",
        caption=(
            "🎙️ **Guest Name:** Ismael Aliyi\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/ACoAADuiUUsBYSewrKAhny3wz2P9NIsQt6AfLcY/)\n"
            "📖 *Description:* Computer Science Student at Malaysia\n"
            "▶️ [Listen on Telegram](https://t.me/TechInEthio/552)"
        ),
        parse_mode="Markdown",
    )

async def episode_e09(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E09")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/C4E03AQFv3gyXEwq6jA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1647553639228?e=1740009600&v=beta&t=7RcefXbkNbmOduWyau7FkR97K9PWI7C-4HhXwSrex1g",
        caption=(
            "🎙️ **Guest Name:** Dr. Menore Tekeba \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/menoretekeba/)\n"
            "📖 *Description:* ML/AI Lecturer and Researcher.\n"
            "▶️ [Watch on YouTube](https://youtu.be/plGJ1g87800)"
        ),
        parse_mode="Markdown",
    )

async def episode_e10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E05")
    
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQEmVA5bcnaneQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1727977457323?e=1740009600&v=beta&t=fLnRjZmZIKJmrRcbM8D3idKpkSzFOZSuu1vBJa8ZpXA",
        caption=(
            "🎙️ **Guest Name:** Yeabsira Ashebir\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/yeabsra-ashebir-tech-nerd-8a3a80267)\n"
            "📖 *Description:* Software Developer.\n"
            "▶️ [Watch on YouTube](https://youtu.be/5ocNYkEj3fk?si=0e6pKBFHzdemDf05)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQH5XRCg_mefQg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1721898213314?e=1740009600&v=beta&t=tS35KKutcReMXKJjkZFadXreJxxbUwwmFMubEZNDI1g",
        caption=(
            "🎙️ **Guest Name:** Natnael Ashebir\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/natnael-ashebir-438b302b0/)\n"
            "📖 *Description:* Designer.\n"
            "▶️ [Watch on YouTube](https://youtu.be/5ocNYkEj3fk?si=0e6pKBFHzdemDf05)"

        ),
        parse_mode="Markdown",
    )

async def episode_e11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E11")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQHJMgumCDBdsA/profile-displayphoto-shrink_800_800/B4EZOhivW9HAAc-/0/1733582062774?e=1740009600&v=beta&t=gg0f64CEv-xm9YfSvBOg190o6KZFAqn1ySEHtRRQISA",
        caption=(
            "🎙️ **Guest Name:** Yohannes Haile\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/yohannes-haile/)\n"
            "📖 *Description:* Project Manager & iOS Engineer\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampldseE11)"
        ),
        parse_mode="Markdown",
    )

async def episode_e12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E05")
    
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFxph_Za9pkmQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1729414174125?e=1739404800&v=beta&t=gIIhlpen1K8WeYAE7delOHjFvbNkD_9kLdgQ1XQv9ak",
        caption=(
            "🎙️ **Guest Name:** Birhanu Yilma\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/dawitsishuhhhjhjh/)\n"
            "📖 *Description:* Co-founder of Dengene Technology Solutions.\n"
            "▶️ [Watch on YouTube](https://www.youtube.com/watch?v=gX8UWy6PMZw&t=1243s)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQHGo7FcfFPK_w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1721247596158?e=1739404800&v=beta&t=pKCAaMPmPthF4AUycWnmMsRhwhA6CRqCJ5r26QEPsQ8",
        caption=(
            "🎙️ **Guest Name:** Yehis Girmaselassie\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/zelalemyedseohannes/)\n"
            "📖 *Description:* Co-founder of Dengene Technology Solutions.\n"
            "▶️ [Watch on YouTube](https://www.youtube.com/watch?v=gX8UWy6PMZw&t=1243s)"

        ),
        parse_mode="Markdown",
    )

async def episode_e13(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E05")
    
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E35AQEGHfK1SZc2tA/profile-framedphoto-shrink_800_800/profile-framedphoto-shrink_800_800/0/1711390461855?e=1734966000&v=beta&t=FTxdn6MKTIueBHDIZ6A5l9k_V0q0BMEKBaVHhAICri0",
        caption=(
            "🎙️ **Guest Name:** Kenawak Ibsa\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/kenawak-ibsa-5936721b9/)\n"
            "📖 *Description:* Software Developer.\n"
            "▶️ [Watch on YouTube](https://www.youtube.com/watch?v=8kJrSZP9a3w)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFzPuAzntehxw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1698347538041?e=1740009600&v=beta&t=BgZDjCEfF81OvE-08EbpZYiS5YT91eTgXjCYo4_VM70",
        caption=(
            "🎙️ **Guest Name:** Abubeker Abe\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/abubeker-abe-bb2325285/)\n"
            "📖 *Description:* Designer.\n"
            "▶️ [Watch on YouTube](https://www.youtube.com/watch?v=8kJrSZP9a3w)"

        ),
        parse_mode="Markdown",
    )

async def episode_e14(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E14")
    # First photo and caption
    await update.message.reply_photo(
        photo="https://media.istockphoto.com/id/1290743328/vector/faceless-man-abstract-silhouette-of-person-the-figure-of-man-without-a-face-front-view.jpg?s=612x612&w=0&k=20&c=Ys-4Co9NaWFFBDjmvDJABB2BPePxJwHugC8_G5u0rOk=",
        caption=(
            "🎙️ **Guest Name:** Natnael Abnew\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/natnael-abnew/)\n"
            "📖 *Description:* Civil Engineering Student at AAU.\n"
            "▶️ [Listen on Telegram](https://t.me/TechInEthio/599)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFB2RTPx9V75g/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1713112726771?e=1740009600&v=beta&t=5OUGtXxX-mfBwB1Ouzu1GP2T1fdg1lPdH_7zbuDBV1k",
        caption=(
            "🎙️ **Guest Name:** Temesgen Abdisa\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/temesgen-abdissa-06315a25a/)\n"
            "📖 *Description:* Software Developer.\n"
            "▶️ [Listen on Telegram](https://t.me/TechInEthio/599)"

        ),
        parse_mode="Markdown",
    )



#Season 2






async def episode_e16(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E16")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFFNaV0TiFpAA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1705921998917?e=1740009600&v=beta&t=zefmb67hTKPXLLqrSOS8I2OEVu5I3OxgbCbLAh_laj8",
        caption=(
            "🎙️ **Guest Name:** Dagmawi Esayas\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/dagmawibabi/)\n"
            "📖 *Description:* Creative Developer\n"
            "▶️ [Watch on YouTube](https://youtu.be/21N1x-vJ_gE?si=SJiU7E__SQkCntfa)"
        ),
        parse_mode="Markdown",
    )

async def episode_e17(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E17")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFDXoPc6VaeSQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1729092670480?e=1740009600&v=beta&t=E-eSdHcubqg3yOpG6M15aDdDMsRctbHIdLc2nhUMdHE",
        caption=(
            "🎙️ **Guest Name:** Hope Alemayehu\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/oliviawhite)\n"
            "📖 *Description:*Quantum Software Developer \n"
            "▶️ [Watch on YouTube](https://youtu.be/r9OBm_HekRo?si=kNSYt_VrsegtjXj3)"
        ),
        parse_mode="Markdown",
    )

async def episode_e18(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E18")
    await update.message.reply_photo(
        photo="https://media.istockphoto.com/id/1290743328/vector/faceless-man-abstract-silhouette-of-person-the-figure-of-man-without-a-face-front-view.jpg?s=612x612&w=0&k=20&c=Ys-4Co9NaWFFBDjmvDJABB2BPePxJwHugC8_G5u0rOk=",
        caption=(
            "🎙️ **Guest Name:** Kinfemichael Tariku \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/kinfe-michael-tariku-1497b3201/)\n"
            "📖 *Description:* Software Developer | Farm UI\n"
            "▶️ [Watch on YouTube](https://youtu.be/7NroCNxrOZw?si=fo5oL4B1E5ADqKhk)"
        ),
        parse_mode="Markdown",
    )

async def episode_e19(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E19")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQEvIBBOICLU0g/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1692461664850?e=1740009600&v=beta&t=sPxP2atcNluM1OQYBwm-ZoOJI6OnZZgxs2L0bO7due8",
        caption=(
            "🎙️ **Guest Name:**  kerod Kibatu\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/kerod-kibatu-076390219/)\n"
            "📖 *Description:* AI Engineer.\n"
            "▶️ [Watch on YouTube](https://youtu.be/AJXeBOGGE7U?si=054X_F_t5fs2nuX_)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQG1wUG_kM56Pw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1725760637799?e=1740009600&v=beta&t=-VeY3Iq93nXHcjDQSvNNbwOCi1lS0ddzH-7pghIK6bE",
        caption=(
            "🎙️ **Guest Name:** Abdella Solomon\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/abdella-solomon-7070ab213/)\n"
            "📖 *Description:* Developer | Freelancer | Writer.\n"
            "▶️ [Watch on YouTube](https://youtu.be/AJXeBOGGE7U?si=054X_F_t5fs2nuX_)"

        ),
        parse_mode="Markdown",
    )

async def episode_e20(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E20")
    await update.message.reply_photo(
        photo="https://example.com/guest20.jpg",
        caption=(
            "🎙️ **Guest Name:** Elizabeth Yonas \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/elizabeth-yonas-5900b8262/)\n"
            "📖 *Description:* Software Developer | AI and Machine Learning Enthusiast .\n"
            "▶️ [Watch on YouTube](https://youtu.be/d61RAlZZZ60?si=orPqBGYEL8zF15y5)"
        ),
        parse_mode="Markdown",
    )
async def episode_e21(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E21")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQEvIlhWiE1-_Q/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1690276767689?e=1740009600&v=beta&t=CjE_Zz2KmMpjdPD3JCs70tv8KG_4d_Zg5gHVhrtCwkc",
        caption=(
            "🎙️ **Guest Name:** Amanuael Kebede\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/amanuael-kebede/)\n"
            "📖 *Description:* Software Engineer | Frontend Developer\n"
            "▶️ [Watch on YouTube](https://youtu.be/07H9Sj9ATtE?si=Zh56Rg7LOJunwTeL)"
        ),
        parse_mode="Markdown",
    )

async def episode_e22(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E22")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQH70MvIduBLjg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1690796367491?e=1740009600&v=beta&t=AUYhm-EVMt0Z_c8KH9cNqKD2JcwXwopMw4S65ODjZ8M",
        caption=(
            "🎙️ **Guest Name:** Bereket Engida\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/bekacru/)\n"
            "📖 *Description:* Founder of Better Auth\n"
            "▶️ [Watch on YouTube](https://youtu.be/PK5HgSmm-uM?si=5UqFwU9j6-Lso8ER)"
        ),
        parse_mode="Markdown",
    )

async def episode_e23(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E23")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQEY_Jdgb4-d9g/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1724235226659?e=1740009600&v=beta&t=hkbsjSXKe3HtGVYLeyWmlKo5ccZe-lIUFIixXGXhygA",
        caption=(
            "🎙️ **Guest Name:** Lydia Abraham\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/lydiaabrahamfirew/)\n"
            "📖 *Description:* Electrical and Computer Engineer | Data Science ML and AI Enthusiast| GDSC Alumini\n"
            "▶️ [Watch on YouTube](https://youtu.be/IY_iXb9Iu4s?si=BXn4IixC08ftpoDk)"
        ),
        parse_mode="Markdown",
    )

async def episode_e24(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E24")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4E03AQFFXFZPSZFT2w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1713712321576?e=1740009600&v=beta&t=iWhINBovhKclHiPE8zU-XmWRTckuMrAu4uYI8LEz4jI",
        caption=(
            "🎙️ **Guest Name:**  Biruk Mesfin \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/biruk-mesfin/)\n"
            "📖 *Description:* GDG AASTU Lead.\n"
            "▶️ [Watch on YouTube](https://youtu.be/oqQGBVwV22w?si=8R9qzSelwjSxzz4_)"

        ),
        parse_mode="Markdown",
    )
    
    # Second photo and caption
    await update.message.reply_photo(
        photo="https://media.istockphoto.com/id/1290743328/vector/faceless-man-abstract-silhouette-of-person-the-figure-of-man-without-a-face-front-view.jpg?s=612x612&w=0&k=20&c=Ys-4Co9NaWFFBDjmvDJABB2BPePxJwHugC8_G5u0rOk=",
        caption=(
            "🎙️ **Guest Name:**  Unique Tegegn \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/unique-tegegn-b29073297/)\n"
            "📖 *Description:* GDG AAU Lead\n"
            "▶️ [Watch on YouTube](https://youtu.be/oqQGBVwV22w?si=8R9qzSelwjSxzz4_)"

        ),
        parse_mode="Markdown",
    )

async def episode_e25(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E25")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4D03AQHfoVxQDMwzuA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1726741438222?e=1740009600&v=beta&t=xkqtJrJWwDYgu2vrJ2hGJkSs80zpCXvMZpApTw7ND-I",
        caption=(
            "🎙️ **Guest Name:** Birhan Nega\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/birhan-nega/)\n"
            "📖 *Description:* Fullstack Software developer at Exelia | .NET | Angular | React\n"
            "▶️ [Watch on YouTube]https://youtu.be/5VFoix-UDQA?si=1S5XcIgR_U7JiY2u)"
        ),
        parse_mode="Markdown",
    )

async def episode_e26(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E26")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/C4E03AQGFaRxfl_-ohg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1653867526476?e=1740009600&v=beta&t=5SCFlH-U1_cm51OCxBRjsf63_H5O1Wvh9EeOn5-g-oY",
        caption=(
            "🎙️ **Guest Name:** Henok B. Ademtew \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/henok-b-ademtew)\n"
            "📖 *Description:* ML Research Engineer\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE26)"
        ),
        parse_mode="Markdown",
    )

async def episode_e27(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E27")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4D03AQEcSrEFXxPffw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1725703585921?e=1740009600&v=beta&t=Z-3mpUrqwcPUhL1X8xYKA0dY6QGVNswyxSSt5Vs179c",
        caption=(
            "🎙️ **Guest Name:** Bethelehem Mulugeta\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/bethelehem-mulugeta-0506a21a3/)\n"
            "📖 *Description:* Computer Engineer | Full-stack Developer | Top Rated Plus Upwork Freelancer | AI R & D\n"
            "▶️ [Watch on YouTube](https://youtu.be/UyI0NeKAZ_M?si=pVIL48Yq5DKIYgD0)"
        ),
        parse_mode="Markdown",
    )

async def episode_e28(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E28")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4D03AQG8t2i-dODeGA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1723977653700?e=1740009600&v=beta&t=Bc6GyM8iS6M3yDBbgytrgIxb_YUPO7ttCtoUCq_q6MU",
        caption=(
            "🎙️ **Guest Name:** Yitayew Solomon\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/yitayew-solomon-381900190/)\n"
            "📖 *Description:* Working for Ethiopian Artificial intelligence institute (EAII)\n"
            "▶️ [Watch on YouTube](https://youtu.be/X215MmQ7_jQ?si=wXcOAbquv-Mmx7Be)"
        ),
        parse_mode="Markdown",
    )

async def episode_e29(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E29")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4D03AQFLnmyJGiEWYQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1694551815283?e=1740009600&v=beta&t=4LKzWHWEiFdvhImBxxsxET6MvG06mGKN7gP_kRyFBYI",
        caption=(
            "🎙️ **Guest Name:** Wondwossen Mulugeta \n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/wondisho/)\n"
            "📖 *Description:* Vice President for Institutional Development at Addis Ababa University Former Board Director and Chairman of IT Subcommittee at Zemen Bank\n"
            "▶️ [Watch on YouTube](https://youtu.be/Q31FOwexXCk?si=knEMq92vfik7QHJv)"
        ),
        parse_mode="Markdown",
    )

#season 3




async def episode_e30(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E30")
    await update.message.reply_photo(
        photo="https://media.licdn.com/dms/image/v2/D4D03AQFh44os_ClfCA/profile-displayphoto-shrink_800_800/B4DZN5_XzDG0Ag-/0/1732918477351?e=1740009600&v=beta&t=TmmBBGSVXABfwRiDmMlscnNzxK7mL1oR-MThfXnG1Pg",
        caption=(
            "🎙️ **Guest Name:** Temkin Mengistu\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/chapimenge/)\n"
            "📖 *Description:* Senior Software Developer\n"
            "▶️ [Watch on YouTube](https://youtu.be/kk-p5CFSoRs?si=GmyKddyeAM8CR2pw)"
        ),
        parse_mode="Markdown",
    )

async def episode_e31(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E31")
    await update.message.reply_photo(
        photo="https://example.com/guest31.jpg",
        caption=(
            "🎙️ **Guest Name:** Clara White\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/clarawhite)\n"
            "📖 *Description:* Clara is a renewable energy scientist and innovator.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE31)"
        ),
        parse_mode="Markdown",
    )

async def episode_e32(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E32")
    await update.message.reply_photo(
        photo="https://example.com/guest32.jpg",
        caption=(
            "🎙️ **Guest Name:** David Black\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/davidblack)\n"
            "📖 *Description:* David is a venture capitalist and tech entrepreneur.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE32)"
        ),
        parse_mode="Markdown",
    )

async def episode_e33(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E33")
    await update.message.reply_photo(
        photo="https://example.com/guest33.jpg",
        caption=(
            "🎙️ **Guest Name:** Emma Yellow\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/emmayellow)\n"
            "📖 *Description:* Emma is a machine learning engineer and AI specialist.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE33)"
        ),
        parse_mode="Markdown",
    )

async def episode_e34(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E34")
    await update.message.reply_photo(
        photo="https://example.com/guest34.jpg",
        caption=(
            "🎙️ **Guest Name:** Frank Violet\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/frankviolet)\n"
            "📖 *Description:* Frank is a blockchain developer and cryptocurrency expert.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE34)"
        ),
        parse_mode="Markdown",
    )