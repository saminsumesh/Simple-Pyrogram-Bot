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
**__⚜️ MEMBERSHIPS DETAILS ⚜️__**

 
**• തെൻകുടം പ്രീമിയം 🔕**
 = __100 Rs__

**• Leaked Videos Only 🍑🍌**
 =  __100 Rs__

**• തെൻകുടം Unlimited 🍑🔞**
= __100 Rs__

**• തെൻകുടം MALLU ONLY 🔞**
= __150 Rs__
"""
ABOUT_TXT = """ 
× **Name** : [തെൻകുടം VIP Bot](https://t.me/thenkudamvipbot)

"""
START_TXT = """
**Hi {} 🌝,\n
Welcome to Thenkudam VIP BOT 🍑**\n

**__Premium Thund Bot__**
"""

HELP_TXT = """
🇬🇧 __ENGLISH__
**• YOU CAN PURCHASE VIP ACCESS OF OUR THENKUDAM VIP CHANNEL 🍑.**\n
🇮🇳 __MALAYALAM__
**• തെൻകുടം ചാനലിൻ്റെ VIP നിങ്ങൾക്ക് ഈ ബോട്ട് വഴി എടുക്കാം 🍑.**\n
🇮🇳 __HINDI__
**• Tobe Added 🔜**
"""
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        photo=START_PIC,
        caption=START_TXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ഫ്രീ ഡെമോ 🍑", callback_data="demo")
                ],[
                InlineKeyboardButton("വീഡിയോസ് ഗ്രൂപ്പ് 🔞", callback_data="group")
                ],[
                InlineKeyboardButton("Help ❓", callback_data="help")
                ],[
                InlineKeyboardButton("Admin 👮‍♂️", callback_data="admin"),
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
                InlineKeyboardButton("ഫ്രീ ഡെമോ 🍑", callback_data="demo")
        ],[
                InlineKeyboardButton("വീഡിയോസ് ഗ്രൂപ്പ് 🔞", callback_data="group")
                ],[
                InlineKeyboardButton("Help ❓", callback_data="help"),
],[
                InlineKeyboardButton("Admin 👮‍♂️", callback_data="admin"),
                ]]
        )
    )
@Bot.on_callback_query(filters.regex("demo"))
async def about(bot, update):
        await bot.send_photo(photo="AgACAgUAAxkBAAP4Zc6vpwbfBRUixIKZ7VKdpEjumlQAApG7MRsCnuhVyeY12951ljoACAEAAwIAA3kABx4E", caption="Demo 🍑",chat_id=update.from_user.id,
               reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Pay 💸", callback_data="qr_data"), InlineKeyboardButton("Back 🔙", callback_data="del")]])
        )

@Bot.on_callback_query(filters.regex("group"))
async def group(bot, update):
        await bot.send_message(
                text=GROUP_TXT, chat_id=update.from_user.id,
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Pay 💸", callback_data="qr_data"), InlineKeyboardButton("Demo 🍑", callback_data="demo")],[InlineKeyboardButton("Back 🔙", callback_data="start")]])
        )
@Bot.on_callback_query(filters.regex("del"))
async def delete(bot, update):
        await update.message.delete()
        
@Bot.on_callback_query(filters.regex("help"))
async def help(bot, update):
        await bot.send_message(
                text = HELP_TXT, chat_id=update.from_user.id,
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="start")]])
        )
@Bot.on_callback_query(filters.regex("admin"))
async def admin(bot, update):
        await bot.send_message(
                text = "**📩 Message To Admin @hxhall", chat_id=update.from_user.id,
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="start")]])
        )
Bot.run()
