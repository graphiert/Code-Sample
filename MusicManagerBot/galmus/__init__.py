import asyncio
import importlib
from pyrogram import Client
from galmus import config

SUDO_USERS = config.SUDO_USERS
OWNER_ID = config.OWNER_ID

app = Client(
    "galihmusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)


def all_info(app, client):
    global config.BOT_ID, config.BOT_NAME, config.BOT_USERNAME
    global config.ASSID, config.ASSNAME, config.ASSUSERNAME
    getme = app.get_me()
    getme1 = client.get_me()
    config.BOT_ID = getme.id
    config.ASSID = getme1.id
    if getme.last_name:
        config.BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        config.BOT_NAME = getme.first_name
    config.BOT_USERNAME = getme.username
    config.ASSNAME = (
        f"{getme1.first_name} {getme1.last_name}"
        if getme1.last_name
        else getme1.first_name
    )
    config.ASSUSERNAME = getme1.username


app.start()
client.start()
all_info(app, client)
