import os

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


class Development(Var):
    LOGGER = True
