import re
import random
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd, sudo_cmd
import asyncio
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
import os
from hellbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="animehub ?(.*)"))
@bot.on(sudo_cmd(pattern="animehub ?(.*)", allow_sudo=True))
async def _(event):
    try:
       await event.client(ImportChatInviteRequest('VlC_xPZHL9LXUsMn'))
    except UserAlreadyParticipantError:
        pass
    except:
        await event.reply("You need to join [this](https://t.me/joinchat/VlC_xPZHL9LXUsMn) channel for this module to work.", link_preview=False)
        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter anime name`")
        return
    chat = -1001448132548
    current_chat = event.chat_id
    current_msg = event.id
    try:
       async for event in event.client.iter_messages(chat, search=args, limit=1):
                    await bot.forward_messages(current_chat, event)
    except:
             await event.reply("`Anime not found. Make sure you give correct name`")
             return
    await event.client.delete_messages(current_chat, current_msg)

@bot.on(admin_cmd(pattern="ganime ?(.*)"))
@bot.on(sudo_cmd(pattern="ganime ?(.*)", allow_sudo=True))
async def _g(event):
    try:
       await event.client(ImportChatInviteRequest('VlC_xPZHL9LXUsMn'))
    except UserAlreadyParticipantError:
        pass
    except:
        await event.reply("You need to join [this](https://t.me/joinchat/VlC_xPZHL9LXUsMn) channel for this module to work.", link_preview=False)
        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter anime name`")
        return
    chat = -1001307222870
    current_chat = event.chat_id
    current_msg = event.id
    try:
       async for event in event.client.iter_messages(chat, search=args, limit=1):
                    await bot.forward_messages(current_chat, event)
    except:
             await event.reply("`Anime not found. Make sure you give correct name`")
             return
    await event.client.delete_messages(current_chat, current_msg)


@bot.on(admin_cmd(pattern="animedl ?(.*)"))
@bot.on(sudo_cmd(pattern="animedl ?(.*)", allow_sudo=True))
async def _get(event):
    try:
       await event.client(ImportChatInviteRequest('VlC_xPZHL9LXUsMn'))
    except UserAlreadyParticipantError:
        pass
    except:
        await event.reply("You need to join [this](https://t.me/joinchat/VlC_xPZHL9LXUsMn) channel for this module to work.", link_preview=False)
        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter anime name`")
        return
    chat = -1001392274404
    current_chat = event.chat_id
    current_msg = event.id
    try:
       async for event in event.client.iter_messages(chat, search=args, limit=1):
                    await bot.forward_messages(current_chat, event)
    except:
             await event.reply("`Anime not found. Make sure you give correct name`")
             return
    await event.client.delete_messages(current_chat, current_msg)


@bot.on(admin_cmd(pattern="ecchi ?(.*)"))
@bot.on(sudo_cmd(pattern="ecchi ?(.*)", allow_sudo=True))
async def _g(event):
    try:
       await event.client(ImportChatInviteRequest('VlC_xPZHL9LXUsMn'))
    except UserAlreadyParticipantError:
        pass
    except:
        await event.reply("You need to join [this](https://t.me/joinchat/VlC_xPZHL9LXUsMn) channel for this module to work.", link_preview=False)
        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter anime name`")
        return
    chat = -1001499176427
    current_chat = event.chat_id
    current_msg = event.id
    try:
       async for event in event.client.iter_messages(chat, search=args, limit=1):
                    await bot.forward_messages(current_chat, event)
    except:
             await event.reply("`Anime not found. Make sure you give correct name`")
             return
    await event.client.delete_messages(current_chat, current_msg)


CmdHelp("anime_dl").add_command(
  "animehub", "<anime name>", "Gives the download link of searched anime. Note that search query should be perfectly spelled. Check .anilist <anime name> to get info about that anime and their perfect spelling"
).add_command(
  "ganime", "<anime name>", "Gives the download link of searched anime in GDrive. If <.animehub> fails try this."
).add_command(
  "animedl", "<anime name>", "Gives the download link of searched anime in telegram channels link. Easy to download links."
).add_command(
  "ecchi", "<anime name>", "Gives the download link of searched ecchi anime."
).add_info(
  "Anime Downloader"
).add()
