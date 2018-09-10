from telethon import TelegramClient, events
from async_generator import aclosing
from datetime import datetime, timedelta
import time
import logging
import random, re
import asyncio
import os
from gtts import gTTS
import time
import hastebin
import urbandict
import gsearch
import subprocess
from datetime import datetime
from requests import get
import wikipedia
import inspect
import platform
import pybase64
import pyfiglet
from googletrans import Translator
from random import randint
from zalgo_text import zalgo
import sqlite3

@borg.on(events.NewMessage(pattern='.cp'))
@borg.on(events.MessageEdited(pattern='.cp'))
async def copypasta(e):
    textx=await e.get_reply_message()
    if textx:
         message = textx
         message = str(message.message)
    else:
        message = e.text
        message = str(message[3:])
    emojis = ["😂", "😂", "👌", "✌", "💞", "👍", "👌", "💯", "🎶", "👀", "😂", "👓", "👏", "👐", "🍕", "💥", "🍴", "💦", "💦", "🍑", "🍆", "😩", "😏", "👉👌", "👀", "👅", "😩", "🚰"]
    reply_text = random.choice(emojis)
    b_char = random.choice(message).lower() # choose a random character in the message to be substituted with 🅱️
    for c in message:
        if c == " ":
            reply_text += random.choice(emojis)
        elif c in emojis:
            reply_text += c
            reply_text += random.choice(emojis)
        elif c.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(random.getrandbits(1)):
                reply_text += c.upper()
            else:
                reply_text += c.lower()
    reply_text += random.choice(emojis)
    await e.edit(reply_text)