from bot import DATABASE_URL, BOT_USERNAME
from bot.database import Database

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
