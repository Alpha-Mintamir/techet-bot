# Techet Bot

Welcome to the Tech Bot repository! This bot is designed for the techኢት Telegram channel, a digital media platform where tech-related content is posted. It serves as assistance and automation for the channel.

## Features

- **Main Menu Navigation**: Users can interact with the bot using a custom keyboard, allowing them to select different segments like Daily News, Podcast, Opportunities, Our Service, Ad Booking, About Us, Tech Humor, and Tech Events.
- **Podcast Section**: Provides access to podcasts organized by seasons and episodes.
- **About Us Section**: Includes information about Techet and the team members.
- **Services Menu**: Details about the social media management packages offered.
- **Content Forwarding**: Forwards content from the specified Telegram channel to the bot based on the tag used in the channel.
- **Opportunities Menu**: Provides information about job opportunities, internships, and scholarships.
- **Tech Humor Section**: Shares tech-related jokes and memes.
- **Tech Events Section**: Display upcoming tech events and conferences.
- **Ad Booking Section**: Allows users to book ads for the Telegram channel.


## Structure

- `bot/main.py`: Contains the main bot logic, including command handlers and message handlers for various menus and commands like `/start`.
- `features/about_team.py`: Handles the "About the Team" feature, introducing team members with their names, roles, and images.
- `content_forwarding.py`: Manages the forwarding of content from a Telegram channel to users.
- `features/opportunities.py`: Provides information about job opportunities, internships, and scholarships.
- `features/podcast.py`: Manages the podcast section, including the seasons and episodes.
- `features/services.py`: Displays the social media management packages offered by Techet.
- `features/about_techet.py`: Contains information about Techኢት and its services.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Alpha-Mintamir/techet-bot.git
    ```

2. **Navigate to the Bot Directory**:

    ```bash
    cd techet-bot/bot
    ```

3. **Set Up a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```

4. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Environment Variables**:

    Create a `.env` file and add your Telegram bot token and channel ID:

    ```env
    TELEGRAM_BOT_TOKEN=your_bot_token_here
    CHANNEL_ID=your_channel_id_here
    ```

## Usage

Run the bot using the following command:

```bash
python main.py
```

## Dependencies

- **python-telegram-bot**: Used for interacting with the Telegram Bot API.
- **Python 3.7+**: The bot requires Python version 3.7 or higher.
- **python-dotenv**: Used for loading environment variables from a `.env` file.
- **redis**: A key-value store used for caching data.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
