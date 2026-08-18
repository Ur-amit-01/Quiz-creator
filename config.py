"""
config.py — boot-time configuration, read once from the environment.
"""
import re
import os

id_pattern = re.compile(r"^-?\d+$")


def _as_id_list(raw: str):
    """Space-separated string of user ids -> list[int]."""
    out = []
    for item in raw.split():
        item = item.strip()
        if item and id_pattern.match(item):
            out.append(int(item))
    return out


# ---- Telegram credentials --------------------------------------------------
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# ---- Access control ---------------------------------------------------------
# User ids allowed to run /quiz. Space-separated, e.g. "111111 222222"
ADMINS = _as_id_list(os.environ.get("ADMINS", "7150972327"))

# The channel the bot posts quiz polls into. The bot MUST be an admin there
# with "Post messages" rights. Accepts a numeric id (e.g. -1001234567890)
# or a public @username.
CHANNEL_ID_RAW = os.environ.get("CHANNEL_ID", "-1003635200719")
CHANNEL_ID = (
    int(CHANNEL_ID_RAW) if id_pattern.match(CHANNEL_ID_RAW) else CHANNEL_ID_RAW
)

# ---- Misc --------------------------------------------------------------------
PORT = int(os.environ.get("PORT", "8080"))


def missing_required():
    """List of (name, hint) for required env vars that are still unset."""
    problems = []
    if not API_ID:
        problems.append(("API_ID", "your api_id from my.telegram.org"))
    if not API_HASH:
        problems.append(("API_HASH", "your api_hash from my.telegram.org"))
    if not BOT_TOKEN:
        problems.append(("BOT_TOKEN", "the bot token from @BotFather"))
    if not ADMINS:
        problems.append(("ADMINS", "space-separated user id(s) allowed to run /quiz"))
    if not CHANNEL_ID:
        problems.append(("CHANNEL_ID", "the channel id/username the bot posts quizzes to"))
    return problems
