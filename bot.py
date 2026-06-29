# 1st discord bot

import discord
import random
from discord.ext import commands

# Set up intents and the bot
intents = discord.Intents.default()
intents.message_content = True  # To read the content of messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Rock, Paper, Scissors command
@bot.command()
async def rps(ctx, user_choice: str):
    # Possible choices for the game
    choices = ['rock', 'paper', 'scissors']
    
    # Make user choice lowercase for comparison
    user_choice = user_choice.lower()
    
    if user_choice not in choices:
        await ctx.send("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return
    
    # Bot's choice
    bot_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        result = "You win!"
    else:
        result = "I win!"

    # Send the result to the user
    await ctx.send(f'You chose {user_choice}, I chose {bot_choice}. {result}')

# Run the bot with your token
bot.run('')
