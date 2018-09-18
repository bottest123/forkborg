# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events
from datetime import datetime
from googletrans import Translator


@borg.on(events.NewMessage(pattern=r".tr (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    else:
        lan, text = input_str.split("|")
    translator = Translator()
    translated_text = translator.translate(text, lan).text
    end = datetime.now()
    ms = (end - start).seconds
    output_str = "Translated to {} in {} seconds. \n {}".format(lan, str(ms), translated_text)
    await event.edit(output_str)

    
# For people's Use They can translate Things from you with the below command

@borg.on(events.NewMessage))
async def f(e):
	global tr
	global translate_to
	global translate_group
	print (e.chat_id in translate_group)
	if tr:
		if e.chat_id in translate_group:
			to = translate_to
			await e.edit(trans.translate(e.raw_text, dest=to).text)

@borg.on(events.NewMessage(pattern=".tran (.*)"))
async def tr(e):
        s = e.pattern_match.group(1)
        if e.is_reply: 
        	s = await e.get_reply_message()
        	s = s.message
        	if e.pattern_match.group(1):
        		to = e.pattern_match.group(1)
        	else:
        		to = 'en'
        	text = trans.translate(s, dest=to)
        	frm = languages.get(part1=text.src).name
        	await e.reply('From: '+frm+'\n'+text.text)
        	return
        to = re.findall(r"to=\w+", s)
        try:
        	to = to[0]
        	to = to.replace('to=', '')
        	s = s.replace('to='+to+' ', '')
        	print(s)
        	print('to='+to)
        except IndexError:
        	to = 'en'
        try:
        	text = trans.translate(s, dest=to)
        except:
        	await e.edit("Maybe wrong code name")
        	return
        frm = languages.get(part1=text.src).name
        await e.reply('From: '+frm+'\n'+text.text)
