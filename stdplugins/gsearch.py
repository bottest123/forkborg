from telethon import events, utils, TelegramClient
import requests
import sys, os, re, subprocess, time, logging, math
from datetime import datetime, timedelta

@borg.on(events.NewMessage(pattern=r'.google (.*)'))
@borg.on(events.MessageEdited(pattern=r'.google (.*)'))
async def gsearch(e):
        match = e.pattern_match.group(1)
        result_=subprocess.run(['gsearch', match], stdout=subprocess.PIPE)
        result=str(result_.stdout.decode())
        await borg.send_message(await borg.get_input_entity(e.chat_id), message='**Search Query:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=e.id, link_preview=False)
        