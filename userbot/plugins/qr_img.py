import os
os.system("pip install qr-img")
import qr_img

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from hellbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="qrimg ?(.*)"))
@bot.on(sudo_cmd(pattern="qrimg ?(.*)", allow_sudo=True))
async def _(event):
    tx = event.pattern_match.group(1)
    if not tx:
        return await eor(event, "Give Text")
    await eor(event, "processing")
    p = await event.client.get_profile_photos(bot.me.id)
    if len(p)>=1:
       file = await bot.download_media(p[0])
    else:
       file= "  "
    out = "hellbot.png"
    qr_img.qrpic(event, file, tx, out)
    await bot.send_file(event.chat_id, out, force_document=False)
    await event.delete()


@bot.on(admin_cmd(pattern="qrmark ?(.*)"))
@bot.on(sudo_cmd(pattern="qrmark ?(.*)", allow_sudo=True))
async def _(event):
    tx = event.pattern_match.group(1)
    r = await event.get_reply_message()
    if not (tx and r and r.media):
        return await eor(event, "reply to image and Give Text")
    await eor(event, "processing")
    d = await bot.download_media(r.media)
    out = "hellbot.png"
    qr_img.watermark_qr(event, d, tx, out)
    await bot.send_file(event.chat_id, out, force_document=False)
    await event.delete()
 
    
@bot.on(admin_cmd(pattern="qrdecode$"))
@bot.on(sudo_cmd(pattern="qrdecode$", allow_sudo=True))
async def _(event):
    r = await event.get_reply_message()
    if not (r and r.media):
        return await eor(event, "reply to image and Give Text")
    await eor(event, "processing")
    image = await bot.download_media(r.media)
    tx = qr_img.qr_decode(image)
    await eor(event, "Decoded Text:\n\n" + tx)
    
    
CmdHelp("qr_img").add_command(
  "qrimg", "<reply to a image> <text>", "Makes a qrcode with that image"
).add_command(
  "qrmark", "<reply to image> <text>", "Draws a qr code on the replied image"
).add_command(
  "qrdecode", "<reply to image> <text>", "Decodes the value of replied qr code"
).add_info(
  "QR Codes"
).add()