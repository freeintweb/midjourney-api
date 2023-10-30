from os import getenv

from exceptions import MissRequiredVariableError

GUILD_ID = getenv("GUILD_ID")
CHANNEL_ID = getenv("CHANNEL_ID")
USER_TOKEN = getenv("USER_TOKEN")
CALLBACK_URL = getenv("CALLBACK_URL")
SESSION_ID = getenv("SESSION_ID") \
    or "cb06f61453064c0983f2adae2a88c223"

if not all([GUILD_ID, CHANNEL_ID, USER_TOKEN]):
    raise MissRequiredVariableError("Missing required environment variable: [GUILD_ID, CHANNEL_ID, USER_TOKEN]")
