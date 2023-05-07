## Reddit Bot for Discord

This is a Python script that uses the `discord.py` library to implement a simple Reddit bot for Discord. The bot can fetch the top posts from a given subreddit and display them as embedded images or videos in a Discord chat.

### Features

- Uses the Reddit API to fetch the top posts from a subreddit
- Supports multiple file formats for embedded images and videos, such as GIF, MP4, and WebM
- Can handle Reddit videos and fallback to direct links when necessary
- Includes error handling for invalid commands and missing arguments
- Written in Python 3 and follows PEP 8 style guidelines

### Requirements

- Python 3.x
- `discord.py` library
- `requests` library
- `json` library
- A valid Discord bot token

```
pip3 install discord.py requests json
```

### Getting the bot token
To get a bot token for your Discord bot, you need to create a new application and bot account on the Discord Developer Portal. Here are the steps to follow:

Go to the Discord Developer Portal and log in with your Discord account.

Click on the "New Application" button and enter a name for your application. This name will be visible to users who authorize your bot.

Once you have created the application, click on the "Bot" tab on the left-hand side and click on the "Add Bot" button to create a new bot account.

Customize the bot account by adding a name, avatar, and description. You can also set permissions for the bot to restrict what it can do in Discord servers.

After you have created the bot account, you will see a "Token" section with a button to "Copy" the bot token. Click on the "Copy" button and save the token to a safe place.

To use the bot token in your Python code, replace the placeholder text INSERT_DISCORD_BOT_TOKEN_HERE in the client.run() method call at the end of the code with the actual token you copied from the Discord Developer Portal.

### Usage

To use the bot, simply provide a valid Discord bot token in the `client.run()` method call at the end of the script, and run it with Python 3. The bot will listen for messages starting with the command `!subreddit`, followed by the name of the subreddit to fetch posts from.

For example, to fetch the top posts from the `aww` subreddit, type `!subreddit aww` in a Discord chat where the bot is present.
