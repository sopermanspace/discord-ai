import discord
from discord.ext import commands
import cohere
import asyncio
import nest_asyncio

nest_asyncio.apply()

# Set up the Discord client with non-privileged intents
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

allowed_mentions = discord.AllowedMentions(replied_user=True)
client = commands.Bot(command_prefix='!', intents=intents, allowed_mentions=allowed_mentions)

# Auth with Cohere
cohere_client = cohere.Client(api_key="your-cohere-api-key")

@client.event
async def on_ready():
    print("Discord bot is ready!")

# Function to show the bot is typing
async def show_typing(ctx):
    async with ctx.typing():
        await asyncio.sleep(2)

# Function to get user details
async def get_user_details(ctx):
    user = ctx.author
    username = user.name
    discriminator = user.discriminator
    return f"{username}" #{discriminator}

# Trigger Cohere LLM
@client.command()
async def talk(ctx, *, message):
    # Show the bot is typing
    await show_typing(ctx) 

    # Send the message to Cohere for processing
    response = cohere_client.chat(message=message, model="command")

    user_message = await get_user_details(ctx)

    sent_message = await ctx.send(f"{user_message}\n{response.text}")

# Test using !hello command
@client.command()
async def hello(ctx):
    await ctx.send("Hello! The bot is working!")

# Event to respond when the bot is mentioned
@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and not message.author.bot:
        ctx = await client.get_context(message)
        await talk(ctx, message=message.content.replace(f"<@{client.user.id}>", "").strip())
    await client.process_commands(message)

# Function to start the bot
def run_bot():
    client.run("your-discord-bot-token")

# Run the bot in an asynchronous loop
if __name__ == "__main__":
    run_bot()
