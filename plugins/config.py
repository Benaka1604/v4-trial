import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5968866633:AAE_P4CO8SOWqQF8GvOujfkJpkk3Na0g48o")

    API_ID = int(os.environ.get("API_ID", 23593867))

    API_HASH = os.environ.get("API_HASH", "1f1f4dc0a8a93859adb80c1af3c4bdb5")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1251324232").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @UploadLinkToFileBot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Channakeshava:3NKN96LG@cluster0.ac0uvgi.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001293592327))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1251324232"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001293592327")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ndrk_bot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)
