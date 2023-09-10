import logging

from telethon import TelegramClient

from os import getenv
from NeimanBot.data import NEIMAN


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


API_ID = 27995073
API_HASH = "f57594c795197deecde36a56cc9623a6"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6013725316").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6358121681"))
SUDO_USERS.append(OWNER_ID)



N1 = TelegramClient('N1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
N2 = TelegramClient('N2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
N3 = TelegramClient('N3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
N4 = TelegramClient('N4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
N5 = TelegramClient('N5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
N6 = TelegramClient('N6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
N7 = TelegramClient('N7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
N8 = TelegramClient('N8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
N9 = TelegramClient('N9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
N10 = TelegramClient('N10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
