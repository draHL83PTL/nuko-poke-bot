from typing import Dict
import discord
from intents import nuko_bot_intents
from unite.calculator import Calculator
from words.converter import WordConverter

intents = nuko_bot_intents
client = discord.Client(intents=intents)
prefix = "!nuko"

wc = WordConverter()

@client.event
async def on_message(message):
    if not message.content.startswith(prefix):
        return
    words = [wc.convert(word) for word in wc.word_split(message.content)]
    if len(words) < 2:
        await send_help(message.channel)
        return
    if words[1] == "atkSpd":
        if(len(words) >= 3):
            name = words[2]
            calc = Calculator(name)
            await message.channel.send(calc.red_medal())
            return
    elif words[1] == "help":
        await send_help(message.channel)
        return

async def send_help(channel):
    embed = create_embed_help(
        "!nuko [atkSpd] [pokemon name]",
        "指定したポケモンの攻撃速度を表示する",
        {
            "atkSpd": "「攻撃速度」「as」「attackspeed」でも代用可。",
            "pokemon name": "ポケモンの名前"
        },
        "!nuko 攻撃速度 ピカチュウ"
    )
    await channel.send("**使用可能コマンド**", embed=embed)

def create_embed_help(command, description, args:Dict, example):
    embed = discord.Embed(
        title=command,
        description=description
    )
    for arg_name in args:
        embed.add_field(name=arg_name,value=args.get(arg_name, ""))
    embed.add_field(name="--使用例--",value=example, inline=False)
    return embed

client.run("MTAzMDkyNDUxODQ1OTQ0MTI0Mg.GHgYLX.QsBXw2c7_6b8IYyjlqR2k0OedQ02l2NETdseNc")