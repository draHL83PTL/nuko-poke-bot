import discord

nuko_bot_intents = discord.Intents.default()
nuko_bot_intents.voice_states = True
nuko_bot_intents.message_content = True