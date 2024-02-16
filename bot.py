import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ParseMode

Bot = Client(
"Simple pyrogram bot",
bot_token = os.environ.get("BOT_TOKEN"),
api_hash = os.environ.get("API_HASH"),
api_id = int(os.environ.get("API_ID"))
        )

START_PIC = "AgACAgUAAxkBAAPPZc6ljMGDAAH2fl4RPxTBR7oonoidAAINvjEbPltxVt4mOfli4nbVAAgBAAMCAAN5AAceBA"

GROUP_TXT = """

"""
ABOUT_TXT = """ 
× **Name** : [തെൻകുടം VIP Bot](https://t.me/thenkudamvipbot)

"""
START_TXT = """
**Hi {} ,\n
Welcome to Thenkudam VIP BOT**
"""

HELP_TXT = """
• YOU CAN PURCHASE VIP ACCESS OF OUR THENKUDAM VIP CHANNEL 🍑.\n
• തെൻകുടം ചാനലിൻ്റെ VIP നിങ്ങൾക്ക് ഈ ബോട്ട് വഴി എടുക്കാം 🍑.

"""
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        photo=START_PIC,
        caption=START_TXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("**ഫ്രീ ഡെമോ 🍑**", callback_data="demo"),
                InlineKeyboardButton("**വീഡിയോസ് ഗ്രൂപ്പ് 🔞**", callback_data="group"),
                InlineKeyboardButton("**Admin 👮‍♂️**", callback_data="admin"),
                ]]
        )
    )

@Bot.on_message(filters.forwarded & filters.media)
async def media_id_handler(client, message):
    media = getattr(message, message.media.value)
    await message.reply_text(
        f"<code> {media.file_id} </code>", parse_mode=ParseMode.HTML, quote=True
    )
        
@Bot.on_callback_query(filters.regex("start"))
async def back(bot, update):
    await update.message.edit(
        text=START_TXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ഫ്രീ ഡെമോ 🍑", callback_data="demo"),
                InlineKeyboardButton("വീഡിയോസ് ഗ്രൂപ്പ് 🔞", callback_data="group")
                ],[
                InlineKeyboardButton("Help ❓", callback_data="help"),
                InlineKeyboardButton("Admin 👮‍♂️", callback_data="admin"),
                ]]
        )
    )
@Bot.on_callback_query(filters.regex("demo"))
async def about(bot, update):
        await update.message.edit("Error 304",
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="start")]])
        )

@Bot.on_callback_query(filters.regex("group"))
async def group(bot, update):
        await update.message.edit(
                text=GROUP_TXT,
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Pay 💸", callback_data="qr_data"), InlineKeyboardButton("Demo 🍑", callback_data="demo")]])
        )
@Bot.on_callback_query(filters.regex("help"))
async def help(bot, update):
        await update.message.edit(
                text = HELP_TXT,
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="start")]])
        )
@Bot.on_callback_query(filters.regex("admin"))
async def admin(bot, update):
        await update.message.edit(
                text = "**📩 Message To Admin @hxhall"
        )
Bot.run()
