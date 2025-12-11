import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

message_counts = {}
active_channels = set()
ANCHOR_USER_ID = None

@bot.command()
@commands.has_permissions(manage_channels=True)
async def enable(ctx):
    """Enable the bot in this channel"""
    active_channels.add(ctx.channel.id)
    await ctx.send("✅ Bot enabled in this channel!")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def disable(ctx):
    """Disable the bot in this channel"""
    active_channels.discard(ctx.channel.id)
    await ctx.send("❌ Bot disabled in this channel!")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def setanchor(ctx, user: discord.Member):
    """Set the anchor user who resets the counter"""
    global ANCHOR_USER_ID
    ANCHOR_USER_ID = user.id
    await ctx.send(f"✅ Anchor user set to {user.mention}")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def removeanchor(ctx):
    """Remove the anchor user"""
    global ANCHOR_USER_ID
    ANCHOR_USER_ID = None
    await ctx.send("✅ Anchor user removed")

@bot.command()
async def checkanchor(ctx):
    """Check who the current anchor user is"""
    if ANCHOR_USER_ID:
        user = await bot.fetch_user(ANCHOR_USER_ID)
        await ctx.send(f"Current anchor user: {user.mention}")
    else:
        await ctx.send("No anchor user set")

@bot.event
async def on_message(message):
    # Process commands first
    await bot.process_commands(message)
    
    # Check if channel is active
    if message.channel.id not in active_channels:
        return
    
    if message.author.bot:
        return
    
    channel_id = message.channel.id
    
    # Reset counter if message is from anchor user
    if ANCHOR_USER_ID and message.author.id == ANCHOR_USER_ID:
        message_counts[channel_id] = 0
        return
    
    # Increment counter
    message_counts[channel_id] = message_counts.get(channel_id, 0) + 1
    
    # Create thread at 10 messages
    if message_counts[channel_id] >= 10:
        thread = await message.create_thread(
            name=f"Thread {len(message.channel.threads) + 1}"
        )
        await thread.send("New thread created!")
        message_counts[channel_id] = 0

bot.run(os.getenv('DISCORD_TOKEN'))

