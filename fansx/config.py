import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7966814831").split()))

API_ID = int(os.getenv("API_ID", "26359061"))

API_HASH = os.getenv("API_HASH", "fc31566ed17b5deb1c0a527e1176fd76")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8560462661:AAGNXsBfvG3TM2UtR884ZkGjTtLeMt5Npl0")

OWNER_ID = int(os.getenv("OWNER_ID", "7614305342"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003192483568").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://renaldyardiansah6_db_user:5SDoejBCZVmsXE6P@userbot.nozunin.mongodb.net/?appName=Userbot")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003582847922"))
