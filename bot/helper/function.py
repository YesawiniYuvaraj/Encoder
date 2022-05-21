import pyrogram
import asyncio
from bot.helper.devtools import progress_for_pyrogram
import time
import subprocess
from bot import app, sudo_users, ffmpeg


filetype = True

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
  await message.reply_text(f"**The Set Code Is**\n```{ffmpeg[0]}```")

async def upload_mode(app, message):
  mode = message.text.split(" ", maxsplit=1)[1]
 if mode == "document":
   await message.reply_text("Change To Document Upload Mode")
   filetype = False
 elif mode == "video":
   await message.reply_text("Set To Video Mode")
   filetype = True
 else:
   await message.reply_text("Undefined Video Mode Ise ```document``` Or ```video```")

async def upload_handle(app, message, og, thumb, reply_id, msg, u_start, width, height, duration2):
   if filetype == True:
    u_start = time.time()
    await app.send_video(
               video=og,
               chat_id=message.chat.id, 
               supports_streaming=True,
               file_name=og, 
               thumb=thumb, 
               duration=duration2, 
               width=width, 
               height=height, 
               caption=og, 
               reply_to_message_id=reply_id,
               progress=progress_for_pyrogram,
               progress_args=(
                 app,
                 "**⬆️ Trying To Upload ⬆️**",
                 msg,
                 u_start
        )
      )
   else:
    await app.send_document(
               document=og,
               chat_id=message.chat.id, 
               supports_streaming=True,
               file_name=og, 
               thumb=thumb,  
               caption=og, 
               reply_to_message_id=reply_id,
               progress=progress_for_pyrogram,
               progress_args=(
                 app,
                 "**⬆️ Trying To Upload ⬆️**",
                 msg,
                 u_start
        )
      )
   
