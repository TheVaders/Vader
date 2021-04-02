import os
import sys
import asyncio
from os import execl
from time import sleep

from hellbot.utils import admin_cmd, edit_or_reply as eor, sudo_cmd
from hellbot.cmdhelp import CmdHelp
from hellbot import HEROKU_APP, bot

@bot.on(admin_cmd(pattern="restart$"))
@bot.on(sudo_cmd(pattern="restart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await eor(event, "Restarting **[ ░░░ ]** ...\nType `.ping` to check if I am working...")
    await eor(event, "Restarting **[ █░░ ]** ...\nType `.ping` to check if I am working...")
    await eor(event, "Restarting **[ ██░ ]** ...\nType `.ping` to check if I am working...")
    await eor(event, "Restarting **[ ███ ]** ...\nType `.ping` to check if I am working...")
    await eor(event, "Restarted  **[  ✓  ]** ...\nType `.ping` to check if I am working...")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `Turning off bot now ... Manually turn me on later` ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


CmdHelp("power_tools").add_command(
  "restart", None, "Restarts your userbot. Redtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add_info(
  "Power Switch For Bot"
).add()
