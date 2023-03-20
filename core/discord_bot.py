import hikari
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

bot = hikari.GatewayBot(token=TOKEN)

@bot.listen()

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:

    if not event.is_human:
        return

    me = bot.get_me()

    if me.id in event.message.user_mentions_ids:
        await event.message.respond("https://raw.githubusercontent.com/grekland/Down-Bad-Bot/main/res/images/image_1.png")

bot.run()