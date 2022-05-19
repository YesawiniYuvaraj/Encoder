import pyrogram
import asyncio
import time
import subprocess
from bot import app, sudo_users, ffmpeg

OK = {}

async def change_ffmpeg(app, message):
  try:
    changeffmpeg = message.text.split(" ", maxsplit=1)[1]
    ffmpeg.insert(0,changeffmpeg)
    await message.reply_text(f"**Successfully Changed The FFMPEG-CODE To**\n```{changeffmpeg}```")
  except Exception as e:
    await message.reply_text(f"Error ```{e}```")

async def movie_mode(app, message):
  try:
    movie_mode = "-i 'https://te.legra.ph/file/e9408e71281cdcb017874.png' -map 0 -filter_complex 'overlay =main_w-(overlay_w+10):main_h-(overlay_h+10)'  -c:v libx265 -crf 27 -c:s copy -s 854x480 -preset medium -pix_fmt yuv420p10 -metadata title='Visit For More Movies [t.me/AniXpo]'  -metadata:s:v title='Visit Website[Anixpo] t.me/AniXpo] - 480p - HEVC - 8bit'  -metadata:s:a title='[Visit t.me/AniXpo] - Opus - 60 kbps' -metadata:s:s title='[AniXpo Substations Alpha]' -c:a libopus -ab 60k"
    ffmpeg.insert(0,movie_mode)
    await message.reply_text(f"**Successfully Enabled MOVIE 🎥 MODE 📳**")
  except Exception as e:
    await message.reply_text(f"Error ```{e}```")

async def anime_mode(app, message):
    try:
      anime_code = "-i 'https://te.legra.ph/file/e9408e71281cdcb017874.png' -map 0 -filter_complex 'overlay =main_w-(overlay_w+10):main_h-(overlay_h+10)'  -c:v libx265 -crf 30 -c:s copy -s 854x480 -preset slow -metadata title='Visit For More Movies [t.me/AniXpo]'  -metadata:s:v title='Visit Website[Anixpo] t.me/AniXpo] - 480p - HEVC - 8bit'  -metadata:s:a title='[Visit t.me/AniXpo] - Opus - 60 kbps' -metadata:s:s title='[AniXpo Substations Alpha]' -c:a libopus -ab 60k"
      ffmpeg.insert(0,anime_code)
      await message.reply_text("**Enabled Anime Mode**")
    except Exception as e:
      await message.reply_text(f"**Error** ```{e}```")
  
async def get_ffmpeg(app, message):
  await message.reply_text(f"**The Set Code Is**\n{ffmpeg[0]}")
  
def hbs(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "B", 1: "K", 2: "M", 3: "G", 4: "T", 5: "P"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"
  
  
def code(data):
    OK.update({len(OK): data})
    return str(len(OK) - 1)


def decode(key):
    if OK.get(int(key)):
        return OK[int(key)]
    return
