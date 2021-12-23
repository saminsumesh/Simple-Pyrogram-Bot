import os 
from pyrogram import Client, filters

Bot = Client(
"Simple pyrogram bot",
bot_token = os.environ.get("BOT_TOKEN"),
api_hash = os.enivron.get("API_HASH"),
api_id = int(os.environ.get("API_ID"))
        )

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
    text=f"HI {update.from_user.mention}"
    )
    
Bot.run()
