import cv2
import numpy as np
import math
from vcam import vcam,meshGen
import sys
import os
from hellbot.utils import admin_cmd, edit_or_reply as eor, sudo_cmd
from hellbot.cmdhelp import CmdHelp


if not os.path.isdir("./hellbot/"):
    os.makedirs("./hellbot/")
    
    
@bot.on(admin_cmd(pattern=r"funimg"))
@bot.on(sudo_cmd(pattern=r"funimg", allow_sudo=True))
async def fun(event):
    if event.fwd_from:
        return
    path = "omk"
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    await eor(event, "Mirroring In Progress...")
    file_name = "mirror.jpg"
    hehe = path + "/" + file_name
    img = cv2.imread(lol)
    H,W = img.shape[:2]
    fps = 30
    c1 = vcam(H=H,W=W)
    plane = meshGen(H,W)
    plane.Z -= 100*np.sqrt((plane.X*1.0/plane.W)**2+(plane.Y*1.0/plane.H)**2)
    pts3d = plane.getPlane()
    pts2d = c1.project(pts3d)
    map_x,map_y = c1.getMaps(pts2d)
    output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
    output = cv2.flip(output,1)
    out1 = cv2.resize(output,(700,350))
    cv2.imwrite(file_name,out1)
    await bot.send_file(event.chat_id, file_name)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
    hoi = await event.delete()



@bot.on(admin_cmd(pattern=r"funimg2"))
@bot.on(sudo_cmd(pattern=r"funimg2", allow_sudo=True))
async def fun(event):
    if event.fwd_from:
        return
    path = "omk"
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    await eor(event, "Mirroring In Progress...")
    file_name = "mirror.jpg"
    hehe = path + "/" + file_name
    img = cv2.imread(lol)
    H,W = img.shape[:2]
    fps = 30
    c1 = vcam(H=H,W=W)
    plane = meshGen(H,W)
    plane.Z += 20*np.exp(-0.5*((plane.Y*1.0/plane.H)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
    pts3d = plane.getPlane()
    pts2d = c1.project(pts3d)
    map_x,map_y = c1.getMaps(pts2d)
    output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
    output = cv2.flip(output,1)
    out1 = cv2.resize(output,(700,350))
    cv2.imwrite(file_name,out1)
    await bot.send_file(event.chat_id, file_name)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
    hoi = await event.delete()



@bot.on(admin_cmd(pattern=r"funimg3"))
@bot.on(sudo_cmd(pattern=r"funimg3", allow_sudo=True))
async def fun(event):
    if event.fwd_from:
        return
    path = "omk"
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    await eor(event, "Mirroring In Progress...")
    file_name = "mirror.jpg"
    hehe = path + "/" + file_name
    img = cv2.imread(lol)
    H,W = img.shape[:2]
    fps = 30
    c1 = vcam(H=H,W=W)
    plane = meshGen(H,W)
    plane.Z += 20*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
    pts3d = plane.getPlane()
    pts2d = c1.project(pts3d)
    map_x,map_y = c1.getMaps(pts2d)
    output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
    output = cv2.flip(output,1)
    out1 = cv2.resize(output,(700,350))
    cv2.imwrite(file_name,out1)
    await bot.send_file(event.chat_id, file_name)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
    hoi = await event.delete()


CmdHelp("fun_img").add_command(
  "funimg", "<reply to a img/stcr>", "Edits the replied image or sticker to a 3-D Box like image."
).add_command(
  "funimg2", "<reply to a img/stcr>", "Edits the replied image or sticker to a funny image. `#Must_Try` !!"
).add_command(
  "funimg3", "<reply to a img/stcr>", "Edits the replied image or sticker to a funny image. `#Must_Try` !!"
).add_info(
  "Funs are here boiz"
).add()