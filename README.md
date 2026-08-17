# Quiz Bot (demo)

Admin sends `/quiz` to the bot → bot posts one random native Telegram quiz
poll (auto-graded, 60s timer, shows the correct answer once it closes) to a
channel it's admin of.

This is a demo: `questions.py` has 10 questions hardcoded, taken from
`NEET_Biology_AllYears.md` (AIPMT 2011, Q.1–Q.10). There is no database, no
file parser, and no scheduler — every `/quiz` picks one random entry from
that fixed list of 10. Once you've confirmed this works end-to-end, the next
real step is a script that parses the full `.md` file into the same
`{question, options, correct_option_id, explanation}` shape so the pool isn't
stuck at 10 — say the word and I'll build that part.

## Setup

1. Get `API_ID` / `API_HASH` from https://my.telegram.org
2. Get `BOT_TOKEN` from @BotFather
3. Add the bot to your channel as **admin** with "Post messages" enabled
4. Get the channel's numeric id (or use its `@username` if public)
5. Set environment variables:

```
API_ID=...
API_HASH=...
BOT_TOKEN=...
ADMINS=123456789        # your Telegram user id — space-separated for multiple
CHANNEL_ID=-1001234567890
```

6. Run locally:

```
pip install -r requirements.txt
python bot.py
```

Or with Docker:

```
docker build -t quiz-bot .
docker run --env-file .env quiz-bot
```

## Known limitations (on purpose, for a demo)

- Only 10 hardcoded questions — no parsing of the .md file yet.
- `/quiz` posts to one fixed channel (`CHANNEL_ID`), not multiple.
- No cooldown/rate-limit — an admin can spam `/quiz` repeatedly.
- No duplicate-avoidance — the same question can come up twice in a row.
- Bots cannot receive `/quiz` typed by regular members *inside* a channel —
  only admins can post/run commands there. `/quiz` must be sent to the bot
  in a private chat or a group it's in.
