
import os
import logging
from logging.handlers import RotatingFileHandler

#Don't Edit Anything [Support @im_piro | @PiroHackz]

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "704608XL3cXiHthuk5z-X7CXze7-2e7eU-otO8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "104103"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c1003f5d2bf6977c6b80f376eb9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002096197"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "81916"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://RbyThot:Radpff9m.mongoretryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "RbyTot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-10092747"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "tnvalue.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "96bc75957ae5589ca303c32373e")

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝗛𝗲𝗹𝗹𝗼 {mention}👋  𝗜 𝗛𝗮𝘃𝗲 𝗔𝗹𝗹 #𝗧𝗵𝗲𝗮𝘁𝗿𝗲 𝗠𝗼𝘃𝗶𝗲𝘀  𝗪𝗶𝘁𝗵 𝗔𝗹𝗹 𝗤𝘂𝗮𝗹𝗶𝘁𝗶𝗲𝘀 ... 🔥       «【  𝗙𝗼𝗿 𝗡𝗲𝘄 𝗠𝗼𝘃𝗶𝗲𝘀 ➳ @RbyLinkzz⚡ 】»  𝗦𝗵𝗮𝗿𝗲 𝗔𝗻𝗱 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ❣️.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel [@RbyLinkzz⚡]  to use me...\n\nKindly Please join Channel 🙏</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! Contact 🔔 𝗔𝗱𝗺𝗶𝗻 🤖 = @RbyAdminBot ⚡"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
