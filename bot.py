import os 
from pyrogram import Client, filters

Bot = Client(
    "Simple pyrogram bot"
    bot_token = os.environ.get("BOT_TOKEN")
    api_hash = int(os.enivron.get("API_HASH"),
    api_key = os.environ.get("API_KEY")
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
    text=f"HI {update.from_user.mention}
  )
    
    Bot.run()
