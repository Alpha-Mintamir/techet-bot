from telegram import Update
from telegram.ext import ContextTypes

# Package Descriptions
package_one_description = """
🎁 Package 1: 15,000 Birr

This package includes social media management with video content. It covers:
- Full management of your social media profiles (content creation, scheduling, engagement monitoring).
- Monthly reports on social media performance.
- Professionally created video content to be used on your social platforms, designed to boost engagement and visibility.

Ideal for businesses looking for a comprehensive social media presence with high-quality video content.
"""

package_two_description = """
🎁 Package 2: 10,000 Birr

This package includes social media management with a graphic designer. It covers:
- Full management of your social media profiles (content creation, scheduling, engagement monitoring).
- High-quality visuals created by a professional graphic designer for your social media posts.
- Monthly performance reports and analytics.

Perfect for businesses that want to maintain an active social media presence with eye-catching visuals.
"""

package_three_description = """
🎁 Package 3: 7,000 Birr

This is our basic social media management package. It includes:
- Management of your social media accounts, including post creation and scheduling.
- Engagement monitoring and performance reporting.

This package is ideal for businesses looking to maintain a consistent presence on social media at a lower cost. Note: This package does not include a graphic designer or video content.
"""

# Pricing for each package
package_one_price = "💰 Price: 15,000 Birr"
package_two_price = "💰 Price: 10,000 Birr"
package_three_price = "💰 Price: 7,000 Birr"

async def package_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"{package_one_description}\n{package_one_price}"
    )

async def package_two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"{package_two_description}\n{package_two_price}"
    )

async def package_three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"{package_three_description}\n{package_three_price}"
    )

