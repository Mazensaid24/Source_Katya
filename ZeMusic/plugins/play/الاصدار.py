import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5fe893bc2fafc971178c9.mp4",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس كاتيا
★᚜ اسم سورس : كاتيا

★᚜ نوع : ميوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : كارولين بوت ميوزك
★᚜ الاصدار 2.0.14
★᚜ تاريخ التأسيس : 2024/2/2

★᚜ مؤسس كاتيا : [ 《 𝗠 𝗮 𝗭 𝗲 𝗡 》](https://t.me/Ve_G4)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔", url=f"https://t.me/Source_Katya"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

