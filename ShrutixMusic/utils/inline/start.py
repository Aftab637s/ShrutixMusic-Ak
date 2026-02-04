from pyrogram.types import InlineKeyboardButton
import config
from ShrutixMusic import nand

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚",
                url=f"https://t.me/{nand.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ 🎧", url=config.SUPPORT_CHAT
            ),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚",
                url=f"https://t.me/{nand.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💡 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs 💡", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🚀 ᴜᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="☁️ sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴏᴡɴᴇʀ 👑", user_id=config.OWNER_ID
            )
        ],
    ]
    return buttons
    
