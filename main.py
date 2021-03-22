import asyncio
import os
import time

from telethon import events, TelegramClient

try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

#===================================CONSTANTS=================================

API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)


token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)

Hellbot = TelegramClient("hellbot", API_ID, API_HASH).start(bot_token=token)

HellBot = Client("HELLBOT", api_id=API_ID, api_hash=API_HASH, bot_token=token)


if __name__=="__main__":
  Hellbot.run_until_disconnected()

if __name__=="__main__":
  HellBot.start()
