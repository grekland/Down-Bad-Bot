import hikari
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

bot = hikari.GatewayBot(token=TOKEN,banner=None)
