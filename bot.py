import asyncio
import logging
import sys

from pyrogram import Client, filters
from pyrogram.enums import PollType
from pyrogram.types import Message

import config
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS, CHANNEL_ID
from Questions import ALL_QUESTIONS, get_random_quiz

QUIZ_BATCH_SIZE = 10
# Telegram poll question limit is 300 chars; leave room for the "N. " prefix
# and " (YYYY)" suffix we add around the raw question text.
POLL_QUESTION_LIMIT = 300
SECONDS_BETWEEN_POLLS = 3  # be nice to Telegram's flood limits

RESULTS_PROMPT = (
    "10 me se kitne correct kiye ? Aur kal 10 baje ready rahna quiz ke liye"
)

class _PollOpt:
    """
    Minimal stand-in for pyrogram's InputPollOption.

    Some pyrofork builds have a send_poll() that internally reads
    option.text / option.entities off whatever is in the `options` list,
    but don't actually export an importable InputPollOption class yet.
    Rather than depend on that import succeeding, just hand it something
    with the two attributes it wants.
    """
    __slots__ = ("text", "entities")

    def __init__(self, text):
        self.text = text
        self.entities = []


def _poll_options(options):
    return [_PollOpt(o) for o in options]


def _format_poll_question(index: int, q: dict) -> str:
    """'S.no (question) (Year)' formatted as e.g. '1. Question text (2019)'."""
    suffix = f" ({q['year']})"
    prefix = f"{index}. "
    question_text = q["question"]

    room = POLL_QUESTION_LIMIT - len(prefix) - len(suffix)
    if room < 0:
        room = 0
    if len(question_text) > room:
        question_text = question_text[: max(room - 1, 0)].rstrip() + "…"

    return f"{prefix}{question_text}{suffix}"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def check_env():
    problems = config.missing_required()
    if not problems:
        return
    logger.warning("⚠️  Missing/empty environment variable(s):")
    for name, hint in problems:
        logger.warning(f"   - {name}  ({hint})")
    logger.error("Cannot start: fix the environment above and restart.")
    sys.exit(1)


app = Client(
    name="quiz_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


@app.on_message(filters.command("quiz") & filters.user(ADMINS))
async def quiz_command(client: Client, message: Message):
    """Admin-only. Posts a batch of 10 random quiz polls (random years) to CHANNEL_ID."""
    quiz_questions = get_random_quiz(QUIZ_BATCH_SIZE)

    posted = 0
    try:
        for i, q in enumerate(quiz_questions, start=1):
            await client.send_poll(
                chat_id=CHANNEL_ID,
                question=_format_poll_question(i, q),
                options=_poll_options(q["options"]),
                type=PollType.QUIZ,
                correct_option_id=q["correct_option_id"],
                explanation=q.get("explanation"),
                is_anonymous=True,
                open_period=60,  # seconds the poll stays open; drop this line for no timer
            )
            posted += 1

            if i < len(quiz_questions):
                await asyncio.sleep(SECONDS_BETWEEN_POLLS)

        await client.send_message(chat_id=CHANNEL_ID, text=RESULTS_PROMPT)
        await message.reply_text(f"✅ Posted {posted} quiz question(s) to the channel.")
    except Exception as e:
        logger.exception("Failed to post quiz")
        await message.reply_text(
            f"❌ Couldn't post the quiz after {posted}/{len(quiz_questions)} question(s): {e}\n"
            "Check that the bot is an admin in CHANNEL_ID with 'Post messages' rights."
        )


@app.on_message(filters.command("quiz") & ~filters.user(ADMINS))
async def quiz_command_denied(client: Client, message: Message):
    await message.reply_text("⛔ Only admins can run /quiz.")


@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    await message.reply_text(
        "Quiz bot online.\nAdmins: send /quiz to post a random quiz poll to the channel."
    )


if __name__ == "__main__":
    check_env()
    from Questions import YEARS
    logger.info(f"Loaded {len(ALL_QUESTIONS)} questions across {len(YEARS)} years ({YEARS[0]}-{YEARS[-1]}).")
    app.run()
    
