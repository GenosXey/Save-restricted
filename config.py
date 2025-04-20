# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24817837"))
API_HASH = getenv("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = getenv("BOT_TOKEN", "7621248081:AAF6Bj-KPGGO-ogDt_43Xt6hv1D7fZQaUIM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7428552084").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://altof2:123Bonjoure@cluster0.s1suq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002376378205")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002647818964"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
