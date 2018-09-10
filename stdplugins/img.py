from telethon import events, utils, TelegramClient
import requests
from google_images_download import google_images_download   #importing the library
import sys, os, re, subprocess, time, logging, math
from datetime import datetime, timedelta

@borg.on(events.NewMessage(pattern=".img (.*)"))
async def img(e):
	await e.edit('Processing...')
	start=round(time.time() * 1000)
	s = e.pattern_match.group(1)
	lim = re.findall(r"lim=\d+", s)
	try:
		lim = lim[0]
		lim = lim.replace('lim=', '')
		s = s.replace('lim='+lim[0], '')
	except IndexError:
		lim = 2
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":s,"limit":lim, "format":"jpg"}   #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	lst = paths[s]
	await borg.send_file(await borg.get_input_entity(e.chat_id), lst)
	end=round(time.time() * 1000)
	msstartend=int(end) - int(start)
	await e.edit("Done. Time taken: "+str(msstartend) + 's')

