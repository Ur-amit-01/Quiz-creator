"""
Questions package — aggregates every questions_<year>.py file in this
folder into one big pool, tagging each question with the year it came
from.

To add a new year later: drop a questions_<year>.py file in this folder
with a top-level `QUESTIONS = [...]` list (same shape as the others).
It will be picked up automatically — nothing else needs to change.

Exposes:
    ALL_QUESTIONS   -> list[dict], every question from every year, each
                        with a "year" key added (int).
    YEARS           -> sorted list[int] of years that were loaded.
    get_random_quiz(n=10) -> list[dict], n random questions (no repeats)
                        drawn from the whole pool (so effectively from
                        random years).
"""

import importlib
import pkgutil
import random
import re

_YEAR_RE = re.compile(r"questions_(\d{4})$")

ALL_QUESTIONS = []
YEARS = []

for _, _module_name, _ in pkgutil.iter_modules(__path__):
    match = _YEAR_RE.match(_module_name)
    if not match:
        continue  # skip anything that isn't a questions_<year>.py file

    year = int(match.group(1))
    module = importlib.import_module(f"{__name__}.{_module_name}")

    questions = getattr(module, "QUESTIONS", None)
    if not questions:
        continue

    for q in questions:
        tagged = dict(q)  # don't mutate the source module's data
        tagged["year"] = year
        ALL_QUESTIONS.append(tagged)

    YEARS.append(year)

YEARS.sort()


def get_random_quiz(n: int = 10):
    """Return n random questions (no duplicates) from the whole pool."""
    n = min(n, len(ALL_QUESTIONS))
    return random.sample(ALL_QUESTIONS, n)
