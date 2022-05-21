import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv

THUMB = "https://te.legra.ph/file/2ebf402cdef8c27ab4648.jpg"
os.system(f"wget {THUMB} -O thumb.jpg")
ffmpeg = []
ffmpeg.append("-i 'w.wav' -map 0 -filter_complex '[0:a]aformat=channel_layouts=stereo,aresample=async=1000[main]; [1:a]atrim=0:4,adelay=9000|9000[wm];[main][wm]amix=inputs=2' -i 'https://te.legra.ph/file/e9408e71281cdcb017874.png' -lavfi "overlay= overlay= main_w-(overlay_w+10):main_h-(overlay_h+10"  -c:v libx265 -crf 29 -c:s copy -s 854x480 -preset faster -metadata title='Visit For More Movies [t.me/AniXpo]'  -metadata:s:v title='Visit Website[Anixpo] t.me/AniXpo] - 480p - HEVC - 8bit'  -metadata:s:a title='[Visit t.me/AniXpo] - Opus - 60 kbps' -metadata:s:s title='[AniXpo Substations Alpha]' -c:a libopus -ab 60k")
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
MAX_MESSAGE_LENGTH = 4096
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
sudo_users.append(1099725030)
sudo_users.append(5089884151)
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "YoungProzphet")

app = Client("nirusaki", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
