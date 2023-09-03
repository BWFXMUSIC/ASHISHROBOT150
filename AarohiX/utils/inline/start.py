from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 ᴏᴜʀ ɢʀᴏᴜᴩ 🥰",
                url=f"https://t.me/+WDNH4yTCWe5jOTI1",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ ʜᴇʟᴩ ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥 sᴇᴛᴛɪɴɢs ❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Bᴀᴅsʜᴀʜ ❤️‍🔥", url=f"https://t.me/Shivans_Raj_BrockenHart"),
            InlineKeyboardButton(
                text="😍 ᴄᴏ ᴏᴡɴᴇʀ 😍", url=f"https://t.me/Sonu2860"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔥 ᴏᴡɴᴇʀ 🔥", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰 sᴜᴩᴩᴏʀᴛ 🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 ᴏᴜʀ ɢʀᴏᴜᴩ 🥰",
                url=f"https://t.me/+WDNH4yTCWe5jOTI1",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺 ʜᴇʟᴩ 🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Bᴀᴅsʜᴀʜ ❤️‍🔥", url=f"https://t.me/Shivans_Raj_BrockenHart"),
            InlineKeyboardButton(
                text="😍 ᴄᴏ ᴏᴡɴᴇʀ 😍", url=f"https://t.me/Sonu2860"
            ),
        ],
        [
            InlineKeyboardButton(text="🔥 ᴏᴡɴᴇʀ 🔥", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰 sᴜᴩᴩᴏʀᴛ 🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="😂 ᴍᴏʀᴇ 😂", url=f"https://t.me/ZiddiXBot"
            ),
           ],
     ]
    return buttons


