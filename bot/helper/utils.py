import os
from bot import data, download_dir, app
import time
import asyncio
from bot.helper.devtools import progress_for_pyrogram, humanbytes , TimeFormatter
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from .ffmpeg_utils import encode, get_thumbnail, get_duration, get_width_height 

async def on_task_complete():
    del data[0]
    if len(data) > 0:
      await add_task(data[0])

async def add_task(message: Message):
    try: 
      d_start = time.time() 
      msg = await message.reply_text("⬇️ **Downloading Video** ⬇️", quote=True)
      filepath = await app.download_media(
        message=message,  
        file_name=download_dir,
        progress=progress_for_pyrogram,
        progress_args=(
          app,
          "**📥 Trying To Downloading 📥**",
          msg,
          d_start
        )
      )
      await msg.delete()
      chatid = message.chat.id
      reply_id = message.id
      og = await encode(filepath, chatid, reply_id)
      if og:
        mesa = await message.reply_text("**⬆️ Starting To Upload**")
        thumb = await get_thumbnail(og)
        width, height = await get_width_height(filepath)
        duration2 = await get_duration(og)
        await mesa.edit("**⬆️ Uploading Video ⬆️**")
        await app.send_video(video=og, chat_id=message.chat.id, supports_streaming=True, file_name=og, thumb=thumb, duration=duration2, width=width, height=height, caption=og, reply_to_message_id=reply_id)
        await mesa.delete()
        os.remove(thumb)
        os.remove(og)
      else:
        await msg.edit("**Error Contact @NIRUSAKIMARVALE**")
        os.remove(filepath)
        os.remove(og)
    except MessageNotModified:
      pass
    except Exception as e:
      await msg.edit(f"```{e}```")
    await on_task_complete()
    os.remove(filepath)
