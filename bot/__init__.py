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
ffmpeg.append("ffmpeg -i '''{}'''  -vf 'drawtext=text='HC CARTOONS':x=10:y=10:fontsize=29:fontcolor=white:' -c:v libx265 -preset ultrafast -crf 27 -pix_fmt yuv420p -s 1280x720  -map 0:v -c:a libopus -b:a 64k -vbr 2 -ac 2 -map 0:a -c:s copy -map 0:s? '''{}''' -y")
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
 LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
except Exception as e:
 LOGS.info("ENV Are Missing")

app = Client("nirusaki", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)
0
data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
