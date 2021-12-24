import os
from pyrogram import Client, filters

Bot = Client(
"Simple pyrogram bot",
bot_token = os.environ.get("BOT_TOKEN"),
api_hash = os.environ.get("API_HASH"),
api_id = int(os.environ.get("API_ID"))
        )


ABOUT_TXT = """ 
× **Name** : [Gouri Hello Bot](https://t.me/gourihellobot)
× **Creator** : [PaulWalker TG](https://t.mr/paulwalker_tg)
× **FrameWork** : [PyroGram](https://pyrogram.org)
× **Language** : [Python](https://python.org)
"""

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
    text=f"HI {update.from_user.mention} , Iam just a simple pyrogram bot , iam the first own project of my developer , really happy to have you here "
    )
    
@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_sticker(
    sticker="CAACAgUAAxkBAAEBi5ZhxIAlGIuYFRVXxXbMAkoe_hOzzQACJgUAAmF36FUlPPqbW2uijh4E"
    )
    
@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
    text=ABOUT_TXT
    )
Bot.run()
