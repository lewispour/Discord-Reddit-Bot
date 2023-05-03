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

```pip3 install discord.py
pip3 install requests
pip3 install json
```

### Usage

To use the bot, simply provide a valid Discord bot token in the `client.run()` method call at the end of the script, and run it with Python 3. The bot will listen for messages starting with the command `!subreddit`, followed by the name of the subreddit to fetch posts from.

For example, to fetch the top posts from the `aww` subreddit, type `!subreddit aww` in a Discord chat where the bot is present.
