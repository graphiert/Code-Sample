from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
ASSID = int(getenv("ASSID"))
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID"))
UPDATE = getenv("UPDATE", "GalonUpdates")
SUPPORT = getenv("SUPPORT", "GalonSupport")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = "https://telegra.ph/file/50a43cdb6445df264b91e.jpg"
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
