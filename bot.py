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
# Telegram's documented poll question limit is 300 chars, but in practice
# (pyrofork 2.3.68 / current Bot API) anything much over ~255 comes back
# as [400 MESSAGE_TOO_LONG], so stay well under it.
POLL_QUESTION_LIMIT = 255
POLL_OPTION_LIMIT = 100
POLL_EXPLANATION_LIMIT = 200  # Telegram's hard cap on poll explanation text

# Room left for the raw question text once the "N. " prefix and " (YYYY)"
# suffix are added. Worst case prefix is "10. " (4 chars) and suffix is
# always " (YYYY)" (7 chars), so budget for the worst case up front —
# questions longer than this are skipped, never truncated.
_MAX_PREFIX_LEN = len(f"{QUIZ_BATCH_SIZE}. ")
_MAX_SUFFIX_LEN = len(" (YYYY)")
QUESTION_TEXT_LIMIT = POLL_QUESTION_LIMIT - _MAX_PREFIX_LEN - _MAX_SUFFIX_LEN

SECONDS_BETWEEN_POLLS = 3  # be nice to Telegram's flood limits

RESULTS_PROMPT = (
    "10 me se kitne correct kiye ? Aur kal 10 baje ready rahna quiz ke liye"
)
QUIZ_STICKER_ID = "CAACAgEAAxkBAAEGNvVqg1PaFB1WK3Nowc3dIyvtX7a0UwACMRQAApO-0wWgdFhBELv-6D0E"

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
    return f"{index}. {q['question']} ({q['year']})"


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
    quiz_questions = get_random_quiz(
        QUIZ_BATCH_SIZE,
        max_question_len=QUESTION_TEXT_LIMIT,
        max_option_len=POLL_OPTION_LIMIT,
        max_explanation_len=POLL_EXPLANATION_LIMIT,
    )

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

            await client.send_sticker(chat_id=CHANNEL_ID, sticker=QUIZ_STICKER_ID)

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

