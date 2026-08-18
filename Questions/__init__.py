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
    get_random_quiz(n=10, max_question_len=None, max_option_len=None,
                    max_explanation_len=None)
                    -> list[dict], n random questions (no repeats) drawn
                        from the whole pool (so effectively from random
                        years). If max_question_len / max_option_len /
                        max_explanation_len are given, questions whose
                        text, any option, or explanation is longer than
                        the corresponding limit are skipped entirely
                        rather than truncated.
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


def _fits(q: dict, max_question_len, max_option_len, max_explanation_len) -> bool:
    if max_question_len is not None and len(q["question"]) > max_question_len:
        return False
    if max_option_len is not None:
        if any(len(o) > max_option_len for o in q["options"]):
            return False
    if max_explanation_len is not None:
        explanation = q.get("explanation") or ""
        if len(explanation) > max_explanation_len:
            return False
    return True


def get_random_quiz(n: int = 10, max_question_len=None, max_option_len=None,
                     max_explanation_len=None):
    """
    Return n random questions (no duplicates) from the whole pool.

    If max_question_len / max_option_len / max_explanation_len are given,
    any question whose text, any of its options, or its explanation is
    longer than the corresponding limit is skipped (not truncated)
    before sampling.
    """
    pool = ALL_QUESTIONS
    if max_question_len is not None or max_option_len is not None or max_explanation_len is not None:
        pool = [
            q for q in ALL_QUESTIONS
            if _fits(q, max_question_len, max_option_len, max_explanation_len)
        ]

    n = min(n, len(pool))
    return random.sample(pool, n)
                         
