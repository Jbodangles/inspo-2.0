import discord
import random
import requests
import json

# Initialization
client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return quote

# Token
token = "OTYyODYxMDI2MjAwNjUzODM0.YlNsNQ.AzrmJwWzUazrLZXFQ7-BvTRvlaY"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/inspire'):
        quote = get_quote()
        await message.channel.send(quote)
# Initialization
client = discord.Client()

jokes = [
  "Mr. Wzrd has the smallest want in all of Omnia",
  "When hugging Mr. Wzrd you tend to hug his head more than his body",
  "When kissing Mr. Wzrd either you have to tiptoe, or the other person has to kneel",
  "Mr. Wzrds legs don't touch the floor when sitting on a stool",
  "Coming down the stairs must feel like skydiving for Mr. Wzrd",
  "Mr. Wzrd is the literal definition of down to earth",
  "Why can't Mr. Wzrd get depressed? He's always looking up!",
  "You know you are smakk when you can do pull-ups on a door handle, just sk Mr. Wzard"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/kitch'):
        get_joke = random.choice(jokes)
        await message.channel.send(get_joke)

client.run(token)
