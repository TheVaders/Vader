"""Available Commands:
.mf"""

import asyncio
import os
import re

from telethon import functions

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"dc"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"dc", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await edit_or_reply(event, result.stringify())


@bot.on(admin_cmd(pattern=r"config"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"config", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @HellBot_Official""")


@bot.on(admin_cmd(pattern="dm ?(.*)"))
@bot.on(sudo_cmd(pattern="dm ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hell = event.pattern_match.group(1)
    kraken = hell.split(" ")
    chat_id = kraken[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    patra = ""
    letter = await event.get_reply_message()
    if event.reply_to_msg_id:
        await bot.send_message(chat_id, letter)
        await edit_or_reply(event, "**[ ✓ Done ]**")
    for i in kraken[1:]:
        patra += i + " "
    if patra == "":
        return
    try:
        await bot.send_message(chat_id, patra)
        await edit_or_reply(event, "**[ ✓ Done ]**")
    except BaseException:
        await edit_or_reply(event, "**Syntax :-** `.dc <username> <message>")


CmdHelp("bot").add_command(
  "dc", None, "Gets the DataCenter Number"
).add_command(
  "config", None, "😒"
).add_command(
  "dm", "<username> <message>", "Sends a DM to given username with required msg", "dm @SupRemE_AnanD Sar U pro"
).add_info(
  "Haa vai? Kya hua?"
).add()
