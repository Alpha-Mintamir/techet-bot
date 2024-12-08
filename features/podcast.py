from telegram import Update, ReplyKeyboardMarkup
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
            "🎙️ **Guest Name:** Bob Brown\n"
            "🔗 [LinkedIn Profile](https://www.linkedin.com/in/abzaek/)\n"
            "📖 *Description:* Software Engineering Student at AAiT.\n"
            "▶️ [Watch on YouTube Part 1](https://youtu.be/xSE0TtkZszM?si=5By51qdKTsHTvV2b)"
            "▶️ [Watch on YouTube Part 2](https://youtu.be/reEm4kzKYFo?si=c8R-DgGQGoBIRAmA)"
            "▶️ [Watch on YouTube Part 3](https://youtu.be/h7mg_Jp11Y0?si=VCgt7JlwSLn8VDnU)"
        ),
        parse_mode="Markdown",
    )


async def episode_e04(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E04")
    await update.message.reply_photo(
        photo="https://example.com/guest4.jpg",
        caption=(
            "🎙️ **Guest Name:** Bob Brown\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/bobbrown)\n"
            "📖 *Description:* Bob is a cybersecurity expert with over 20 years of experience.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE04)"
        ),
        parse_mode="Markdown",
    )

async def episode_e05(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E05")
    await update.message.reply_photo(
        photo="https://example.com/guest5.jpg",
        caption=(
            "🎙️ **Guest Name:** Carol White\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/carolwhite)\n"
            "📖 *Description:* Carol is a pioneer in renewable energy solutions.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE05)"
        ),
        parse_mode="Markdown",
    )

async def episode_e06(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E06")
    await update.message.reply_photo(
        photo="https://example.com/guest6.jpg",
        caption=(
            "🎙️ **Guest Name:** David Green\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/davidgreen)\n"
            "📖 *Description:* David is a renowned data scientist and AI ethicist.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE06)"
        ),
        parse_mode="Markdown",
    )

async def episode_e07(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E07")
    await update.message.reply_photo(
        photo="https://example.com/guest7.jpg",
        caption=(
            "🎙️ **Guest Name:** Emma Blue\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/emmablue)\n"
            "📖 *Description:* Emma is a software engineer specializing in cloud computing.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE07)"
        ),
        parse_mode="Markdown",
    )

async def episode_e08(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E08")
    await update.message.reply_photo(
        photo="https://example.com/guest8.jpg",
        caption=(
            "🎙️ **Guest Name:** Frank Black\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/frankblack)\n"
            "📖 *Description:* Frank is an entrepreneur and venture capitalist.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE08)"
        ),
        parse_mode="Markdown",
    )

async def episode_e09(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E09")
    await update.message.reply_photo(
        photo="https://example.com/guest9.jpg",
        caption=(
            "🎙️ **Guest Name:** Grace Yellow\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/graceyellow)\n"
            "📖 *Description:* Grace is a leading expert in machine learning and AI.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE09)"
        ),
        parse_mode="Markdown",
    )

async def episode_e10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E10")
    await update.message.reply_photo(
        photo="https://example.com/guest10.jpg",
        caption=(
            "🎙️ **Guest Name:** Henry Violet\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/henryviolet)\n"
            "📖 *Description:* Henry is a blockchain developer and cryptocurrency expert.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE10)"
        ),
        parse_mode="Markdown",
    )
async def episode_e11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E11")
    await update.message.reply_photo(
        photo="https://example.com/guest11.jpg",
        caption=(
            "🎙️ **Guest Name:** Irene Pink\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/irenepink)\n"
            "📖 *Description:* Irene is a specialist in IoT and smart cities.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE11)"
        ),
        parse_mode="Markdown",
    )

async def episode_e12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E12")
    await update.message.reply_photo(
        photo="https://example.com/guest12.jpg",
        caption=(
            "🎙️ **Guest Name:** Jack Orange\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/jackorange)\n"
            "📖 *Description:* Jack is a fintech entrepreneur and blockchain expert.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE12)"
        ),
        parse_mode="Markdown",
    )

async def episode_e13(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E13")
    await update.message.reply_photo(
        photo="https://example.com/guest13.jpg",
        caption=(
            "🎙️ **Guest Name:** Karen Red\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/karenred)\n"
            "📖 *Description:* Karen is a cybersecurity analyst and ethical hacker.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE13)"
        ),
        parse_mode="Markdown",
    )

async def episode_e14(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E14")
    await update.message.reply_photo(
        photo="https://example.com/guest14.jpg",
        caption=(
            "🎙️ **Guest Name:** Leo Green\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/leogreen)\n"
            "📖 *Description:* Leo is a data scientist and AI researcher.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE14)"
        ),
        parse_mode="Markdown",
    )

async def episode_e15(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E15")
    await update.message.reply_photo(
        photo="https://example.com/guest15.jpg",
        caption=(
            "🎙️ **Guest Name:** Mia Blue\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/miablue)\n"
            "📖 *Description:* Mia is a cloud computing expert and software engineer.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE15)"
        ),
        parse_mode="Markdown",
    )

async def episode_e16(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E16")
    await update.message.reply_photo(
        photo="https://example.com/guest16.jpg",
        caption=(
            "🎙️ **Guest Name:** Noah Brown\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/noahbrown)\n"
            "📖 *Description:* Noah is a robotics engineer and AI developer.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE16)"
        ),
        parse_mode="Markdown",
    )

async def episode_e17(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E17")
    await update.message.reply_photo(
        photo="https://example.com/guest17.jpg",
        caption=(
            "🎙️ **Guest Name:** Olivia White\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/oliviawhite)\n"
            "📖 *Description:* Olivia is a renewable energy scientist and innovator.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE17)"
        ),
        parse_mode="Markdown",
    )

async def episode_e18(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E18")
    await update.message.reply_photo(
        photo="https://example.com/guest18.jpg",
        caption=(
            "🎙️ **Guest Name:** Paul Black\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/paulblack)\n"
            "📖 *Description:* Paul is a venture capitalist and tech entrepreneur.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE18)"
        ),
        parse_mode="Markdown",
    )

async def episode_e19(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E19")
    await update.message.reply_photo(
        photo="https://example.com/guest19.jpg",
        caption=(
            "🎙️ **Guest Name:** Quinn Yellow\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/quinnyellow)\n"
            "📖 *Description:* Quinn is a machine learning engineer and AI specialist.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE19)"
        ),
        parse_mode="Markdown",
    )

async def episode_e20(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E20")
    await update.message.reply_photo(
        photo="https://example.com/guest20.jpg",
        caption=(
            "🎙️ **Guest Name:** Rachel Violet\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/rachelviolet)\n"
            "📖 *Description:* Rachel is a blockchain developer and cryptocurrency expert.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE20)"
        ),
        parse_mode="Markdown",
    )
async def episode_e21(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E21")
    await update.message.reply_photo(
        photo="https://example.com/guest21.jpg",
        caption=(
            "🎙️ **Guest Name:** Sam Green\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/samgreen)\n"
            "📖 *Description:* Sam is a data scientist and AI researcher.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE21)"
        ),
        parse_mode="Markdown",
    )

async def episode_e22(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E22")
    await update.message.reply_photo(
        photo="https://example.com/guest22.jpg",
        caption=(
            "🎙️ **Guest Name:** Tina Blue\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/tinablue)\n"
            "📖 *Description:* Tina is a cloud computing expert and software engineer.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE22)"
        ),
        parse_mode="Markdown",
    )

async def episode_e23(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E23")
    await update.message.reply_photo(
        photo="https://example.com/guest23.jpg",
        caption=(
            "🎙️ **Guest Name:** Uma Brown\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/umabrown)\n"
            "📖 *Description:* Uma is a robotics engineer and AI developer.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE23)"
        ),
        parse_mode="Markdown",
    )

async def episode_e24(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E24")
    await update.message.reply_photo(
        photo="https://example.com/guest24.jpg",
        caption=(
            "🎙️ **Guest Name:** Victor White\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/victorwhite)\n"
            "📖 *Description:* Victor is a renewable energy scientist and innovator.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE24)"
        ),
        parse_mode="Markdown",
    )

async def episode_e25(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E25")
    await update.message.reply_photo(
        photo="https://example.com/guest25.jpg",
        caption=(
            "🎙️ **Guest Name:** Wendy Black\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/wendyblack)\n"
            "📖 *Description:* Wendy is a venture capitalist and tech entrepreneur.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE25)"
        ),
        parse_mode="Markdown",
    )

async def episode_e26(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E26")
    await update.message.reply_photo(
        photo="https://example.com/guest26.jpg",
        caption=(
            "🎙️ **Guest Name:** Xavier Yellow\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/xavieryellow)\n"
            "📖 *Description:* Xavier is a machine learning engineer and AI specialist.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE26)"
        ),
        parse_mode="Markdown",
    )

async def episode_e27(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E27")
    await update.message.reply_photo(
        photo="https://example.com/guest27.jpg",
        caption=(
            "🎙️ **Guest Name:** Yara Violet\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/yaraviolet)\n"
            "📖 *Description:* Yara is a blockchain developer and cryptocurrency expert.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE27)"
        ),
        parse_mode="Markdown",
    )

async def episode_e28(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E28")
    await update.message.reply_photo(
        photo="https://example.com/guest28.jpg",
        caption=(
            "🎙️ **Guest Name:** Zach Green\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/zachgreen)\n"
            "📖 *Description:* Zach is a data scientist and AI researcher.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE28)"
        ),
        parse_mode="Markdown",
    )

async def episode_e29(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E29")
    await update.message.reply_photo(
        photo="https://example.com/guest29.jpg",
        caption=(
            "🎙️ **Guest Name:** Amy Blue\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/amyblue)\n"
            "📖 *Description:* Amy is a cloud computing expert and software engineer.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE29)"
        ),
        parse_mode="Markdown",
    )

async def episode_e30(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling Episode E30")
    await update.message.reply_photo(
        photo="https://example.com/guest30.jpg",
        caption=(
            "🎙️ **Guest Name:** Brian Brown\n"
            "🔗 [LinkedIn Profile](https://linkedin.com/in/brianbrown)\n"
            "📖 *Description:* Brian is a robotics engineer and AI developer.\n"
            "▶️ [Watch on YouTube](https://youtube.com/watch?v=exampleE30)"
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