import hikari
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

bot = hikari.GatewayBot(token=TOKEN)

@bot.listen()

async def ping(what: hikari.GuildMessageCreateEvent) -> None:
    if not what.is_human:
        return
    
    me = bot.get_me()

    if me.id in what.message.user_mentions_ids:
        await what.message.attachments(rf"..\res\images\image_1.png")

bot.run()