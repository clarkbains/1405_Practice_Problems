import discord

client = discord.Client()


async def processMsg (channel, msg):
    if msg == "Hi":
        await channel.send("Hi There")

@client.event
async def on_ready():
    print('Logged In')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await processMsg (message.channel, message.content[1:])

client.run('your token here')