import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

Bot = Client(
"Simple pyrogram bot",
bot_token = os.environ.get("BOT_TOKEN"),
api_hash = os.environ.get("API_HASH"),
api_id = int(os.environ.get("API_ID"))
        )


ABOUT_TXT = """ 
× **Name** : [തെൻകുടം VIP Bot](https://t.me/gourihellobot)

"""
START_TXT = """
Hi {} , Welcome to Thenkudam VIP BOT
"""

HELP_TXT = """
• YOU CAN PURCHASE VIP ACCESS OF OUR THENKUDAM VIP CHANNEL 🍑.
• തെൻകുടം ചാനലിൻ്റെ VIP നിങ്ങൾക്ക് ഈ ബോട്ട് വഴി എടുക്കാം 🍑.

"""
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        photo="AgACAgUAAxkBAAIrs2XOfBVlVcWYmUrJgTPPcDBCyvDbAAKytzEb9kZoVpVajrBFYePXAQADAgADeQADNAQ",
        caption=START_TXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ഫ്രീ ഡെമോ 🍑", callback_data="demo"),
                InlineKeyboardButton("വീഡിയോസ് ഗ്രൂപ്പ് 🔞", callback_data="group")
                ],[
                InlineKeyboardButton("Help ❓", callback_data="help"),
                InlineKeyboardButton("Admin 👮‍♂️", callback_data="admin"),
                ]]
        )
    )
@Bot.on_callback_query()
async def cb_buttons(bot, CallbackQuery):
        if query.data == "help":
                await bot.reply_message(HELP_TEXT),
                reply_markup = InlinekeyboadMarkup(InlineKeyboardButton("Back 🔙", callback_data="start")),
        elif query.data == "start":
                await bot.reply_photo(
                        photo="AgACAgUAAxkBAAIrs2XOfBVlVcWYmUrJgTPPcDBCyvDbAAKytzEb9kZoVpVajrBFYePXAQADAgADeQADNAQ",
                        caption=START_TXT.format(bot.from_user.mention),
                        reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ഫ്രീ ഡെമോ 🍑", callback_data="demo"),
                InlineKeyboardButton("വീഡിയോസ് ഗ്രൂപ്പ് 🔞", callback_data="group")
                ],[
                InlineKeyboardButton("Help ❓", callback_data="help"),
                InlineKeyboardButton("Admin 👮‍♂️", callback_data="admin"),
                ]]
                )
                )
        elif query.data == "demo":
                await bot.reply_photo(
                        photo="AgACAgUAAxkBAAIruGXOg16e38HqPSkmAAHQAAEoRWwx7_EAApG7MRsCnuhVKIeKGNzikusBAAMCAAN5AAM0BA"                        
                )
            

    
