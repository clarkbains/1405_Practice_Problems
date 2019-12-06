# Practice problem 10


Make a small bot. The goal of this is to make an extremly simple greeter bot, to get you familiar with how to install and use the discord API. Create an API Token following the following tutorial [here](https://www.writebots.com/discord-bot-token/). Run `pip3 install discord.py` on the command line to get an easy to use library to interface with discord. 

Since the scope of some of the elements are far beyond the level of depth of my tutorial, the basic code will be provided below.

Syntax explanation
* `async` before a function means that you can do some fancy tricks with running two functions at the same time, *multithreading*. For the purposes of this tutorial, everything will be used the same as regular functions, but you will need to add await beofore calling an asynchronous function. Also you may call a regular function from an asynchronous function, and an asynchronous function from a asynchronous function (using await), but you cannot easily call a asynchronous function from a regular function.
* `@client.event` is a bit trickier. The discord libary has different events it fires when certain events happen on discord. Preceding the function with this, known as a decorator, helps the discord library find and trigger the right function with the right event
* `discord.Client()` is imported from the discord library, and is not a part of python itself. 



```python
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
```
 
 

 [discord.py reference](https://discordpy.readthedocs.io/en/latest/api.html) You should have all the tools you need for discord.py from the above example, but if you'd like you can look at the documentation. This documentation is what you'd typically expect in terms of difficulty, so don't worry if nothing makes sense.