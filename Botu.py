import discord
from discord.ext import commands
import openai
import os

# ========= CONFIG =========
DISCORD_TOKEN = "MTQ1ODA5MDk3OTU5NTc4MDIxNg.G_8T7h.1TfNfujvKJCLDkT1yXR-wi0vy4DmGjco2ivXzg"
OPENAI_API_KEY = "sk-mnop5678mnop5678mnop5678mnop5678mnop5678"

openai.api_key = OPENAI_API_KEY

# ========= BOT SETUP =========
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# ========= EVENTS =========
@bot.event
async def on_ready():
    print(f"🔥 Bot online as {bot.user}")

# ========= COMMANDS =========

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

@bot.command()
async def time(ctx):
    await ctx.send("⏰ IST Time: 07 Jan 2026 | GMT+5:30")

@bot.command()
async def ai(ctx, *, msg):
    await ctx.trigger_typing()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Tu ek cool Gen Z Indian AI hai, Hinglish me jawab de."
                },
                {
                    "role": "user",
                    "content": msg
                }
            ],
            max_tokens=200
        )

        reply = response.choices[0].message.content
        await ctx.send(reply)

    except Exception as e:
        await ctx.send("⚠️ Error aaya bhai, API check kar")
        print(e)

@bot.command()
async def roast(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Kisko roast kare? Tag kar 😏")
    else:
        await ctx.send(f"{member.mention} tera IQ WiFi ke signal jaisa hai 📶💀")

@bot.command()
async def quiz(ctx):
    await ctx.send("⚡ Rapid Fire: Newton ka 3rd law kya hai?")

@bot.command()
async def help(ctx):
    await ctx.send(
        "**🤖 BOT COMMANDS**\n"
        "`!ping` – test bot\n"
        "`!ai <question>` – AI se baat\n"
        "`!roast @user` – savage mode\n"
        "`!quiz` – brain test\n"
        "`!time` – IST time\n"
    )

# ========= RUN =========
bot.run(DISCORD_TOKEN)