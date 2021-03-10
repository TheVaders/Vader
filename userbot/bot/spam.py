import asyncio
import base64
import os

from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

@hellbot_cmd("spam", is_args=True)
@pitaji
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@hellbot_cmd("bigspam", is_args=True)
@pitaji
async def bigspam(hell):
    if not hell.text[0].isalpha() and hell.text[0] not in ("/", "#", "@", "!"):
        hell_msg = hell.text
        hellbot_count = int(hell_msg[9:13])
        hell_spam = str(hell.text[13:])
        for i in range(1, hellbot_count):
            await hell.respond(hell_spam)
        await hell.delete()
        if LOGGER:
            await hell.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@hellbot_cmd("mspam", is_args=True)
@pitaji
async def tiny_pic_spam(e):

    sender = await e.get_sender()
    me = await e.client.get_me()

    if not sender.id == me.id and not FULL_SUDO:

        return await e.reply("`Sorry sudo users cant access this command..`")

    try:

        await e.delete()

    except:

        pass

    try:

        counter = int(e.pattern_match.group(1).split(" ", 1)[0])

        reply_message = await e.get_reply_message()

        if (
            not reply_message
            or not e.reply_to_msg_id
            or not reply_message.media
            or not reply_message.media
        ):

            return await e.edit("```Reply to a pic/sticker/gif/video message```")

        message = reply_message.media

        for i in range(1, counter):

            await e.client.send_file(e.chat_id, message)

    except:

        return await e.reply(
            f"**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
        )