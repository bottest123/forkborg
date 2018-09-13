import sys
from telethon import TelegramClient, events
import subprocess
from datetime import datetime

@borg.on(events.NewMessage(outgoing=True,pattern='.*'))
@borg.on(events.MessageEdited(outgoing=True))
async def common_outgoing_handler(e):
    find = e.text
    find = str(find[1:])
    if find=="speed":
            l=await e.reply('`Running speed test . . .`')
            k=subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE)
            await l.edit('`' + k.stdout.decode()[:-1] + '`')
            await e.delete()
