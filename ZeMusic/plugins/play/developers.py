import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["ميزو","مازن","مطور السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/06774fa3fedc7fc8fdb75.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[《 𝗠 𝗮 𝗭 𝗲 𝗡 》](https://t.me/Ve_G4)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ve_G4 ❫
◉ 𝙸𝙳      : ❪ `5951674553` ❫
◉ 𝙱𝙸𝙾    : ❪[#𝖱ꫀᥲ️ᥣᥣ𝗒,!Ꭵ ძ᥆ꪀ'𝗍 ᥴᥲ️𝗋ꫀ#ɪ'َᴍ 𓏺 𝗠 𝗮 𝗭 𝗲 𝗡 𓏺 ¹🦅🇪🇬](https://t.me/Source_Katya)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒《 𝗠 𝗮 𝗭 𝗲 𝗡 》", url=f"https://t.me/Ve_G4"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔", url=f"https://t.me/Source_Katya"),
                ],

            ]

        ),

    )
