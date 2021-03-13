import re

from hellbot import bot
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from hellbot.cmdhelp import CmdHelp
from hellbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    hell = kraken.pattern_match.group(1)
    if not hell:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            await edit_or_reply(kraken, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(hell))}")

    await troll[0].click(
        kraken.chat_id,
        reply_to=kraken.reply_to_msg_id,
        silent=True if kraken.is_reply else False,
        hide_via=True,
    )
    await kraken.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
