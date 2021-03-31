import asyncio
import os
import re

from telethon import functions
from telethon.errors.rpcerrorlist import YouBlockedUserError

from hellbot import ALIVE_NAME as AN
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from userbot.cmdhelp import CmdHelp


DEFAULTUSER = str(AN) if AN else "Hell User"

beta = bot.uid 

hell_user = f"[{DEFAULTUSER}](tg://user?id={beta})"

@bot.on(admin_cmd(pattern="insta (.*)"))
@bot.on(sudo_cmd(pattern="insta (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bot = "@instasavegrambot"
    input_str = event.pattern_match.group(1)
    if "www.instagram.com" not in input_str:
        await eor(event, "Well... this is not instagram link... Mind giving a proper instagram link?")
    else:
        kraken = await eor(event, "Trying to download.... please wait!")
    async with event.client.conversation(bot) as conv:
        try:
            first = await conv.send_message("/start")
            response = await conv.get_response()
            second = await conv.send_message(input_str)
            output_op = await conv.get_response()
            last = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await kraken.edit("User Blocked!! Please Unblock @instasavegrambot and try again...")
            return
        await kraken.delete()
        final = await event.client.send_file(
            event.chat_id,
            output_op,
        )
        await final.edit(
            f"📥 InstaGram Video Downloaded By :- {hell_user}")
    await event.client.delete_messages(
        conv.chat_id, [first.id, response.id, second.id, output_op.id, last.id]
    )


@bot.on(admin_cmd(pattern=r"dc"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"dc", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await eor(event, result.stringify())


@bot.on(admin_cmd(pattern=r"config"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"config", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await eor(event, "Telethon UserBot powered by @HellBot_Official")


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
        await eor(event, "**[ ✓ Done ]**")
    for i in kraken[1:]:
        patra += i + " "
    if patra == "":
        return
    try:
        await bot.send_message(chat_id, patra)
        await eor(event, "**[ ✓ Done ]**")
    except BaseException:
        await eor(event, "**Syntax :-** `.dc <username> <message>")


CmdHelp("bot").add_command(
  "dc", None, "Gets the DataCenter Number"
).add_command(
  "config", None, "😒"
).add_command(
  "dm", "<username> <message>", "Sends a DM to given username with required msg", "dm @SupRemE_AnanD Sar U pro"
).add_info(
  "Haa vai? Kya hua?"
).add()

CmdHelp("instagram").add_command(
  "insta", "<link>", "Downloads the provided instagram video/pic from link.", "insta www.instagram.com/yeuehiwnwiqo"
).add_info(
  "Downloader Hai Vro..."
).add()
