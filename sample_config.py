import os
from telethon.tl.types import ChatBannedRights

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DB_URI", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    CMD_HANDLER = os.environ.get("CMD_HANDLER", r".")
    FBAN_LOGGER_GROUP = os.environ.get("FBAN_LOGGER_GROUP", None)
    if FBAN_LOGGER_GROUP != None:
        try:
            FBAN_LOGGER_GROUP = int(FBAN_LOGGER_GROUP)
        except ValueError:
            raise ValueError("Invalid Log Channel ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")
   
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "924138714").split())
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    if LOG_CHANNEL != None:
        try:
            LOG_CHANNEL = int(LOG_CHANNEL)
        except ValueError:
            raise ValueError("Invalid Log Channel ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")
    LOCATION = os.environ.get("LOCATION", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    SUDO_CMD_HANDLER = os.environ.get("SUDO_CMD_HANDLER", r"\.")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Vader")
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001198699233))
    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
    SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
    SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
    DUAL_LOG = os.environ.get("DUAL_LOG", None)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    MAX_ANTI_FLOOD_MESSAGES = 10
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=True
    )
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 5))
    #pm log
    PM_LOG_GRP_ID = os.environ.get("PM_LOG_GRP_ID", None)
    # set to True if you want to log PMs to your LOG_CHANNEL
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
    # send .get_id in your private channel to forward all your Private messages
    TAG_LOGGER = os.environ.get("TAG_LOGGER", None)
    if TAG_LOGGER != None:
        try:
            TAG_LOGGER = int(TAG_LOGGER)
        except ValueError:
            raise ValueError("Invalid Log Channel ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")
    # tag logger needs group id
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    DB_URI = os.environ.get("DB_URI", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    # number of rows of buttons to be displayed in .helpme command
    BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
    #open load
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    # emoji to be displayed  in help .help
    EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", "🔸")
    # VeryStream only supports video formats
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    watermark_path = os.environ.get("watermark_path", None)
    #Google Chrome Stuff
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    #MongoDB
    MONGO_URI = os.environ.get("MONGO_URI", None)
    #alive
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
    #auto bio
    BIO_MSG = os.environ.get("BIO_MSG", None)
    #Lydia API
    LYDIA_API = os.environ.get("LYDIA_API",None)
    UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/thevaders/vader"
    )
    EXTRA_HELLBOT = os.environ.get("EXTRA_HELLBOT", -1001221881562)
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")


class Development(Var):
    LOGGER = True
