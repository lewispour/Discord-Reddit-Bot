import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!subreddit'):
        subreddit = message.content.split()[1]
        url = f"https://www.reddit.com/r/{subreddit}/top/.json"
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.content.decode('utf-8'))

        for post in data['data']['children']:
            if 'redgifs' in post['data']['url']:
                continue

            if 'gifv' in post['data']['url']:
                file_url = post['data']['url'][:-1]
            else:
                file_url = post['data']['url']

            if file_url.endswith(('.gif', '.mp4', '.webm')):
                embed = discord.Embed()
                if post['data'].get('media') and post['data']['media'].get('reddit_video'):
                    # if the post contains a Reddit video
                    video_url = post['data']['media']['reddit_video']['fallback_url']
                    embed.set_video(url=video_url)
                else:
                    embed.set_image(url=file_url)
                await message.channel.send(embed=embed)

client.run('INSERT_DISCORD_BOT_TOKEN_HERE')
