#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original line of fortune-cookie wisdom for a software
developer to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13 stdlib only, deterministic, no network, no randomness.

Candidate lines drafted and judged against the brief's criteria
(in stated order: 1 fortune-cookie wisdom for a developer, 2 reads
like a fortune cookie, 3 true about a developer's day, 4 fresh turn,
5 quiet twist / double meaning):

  a) "Your estimate was right; it was the future that changed its mind."
     -> CHOSEN (65 chars). Estimates are explicitly named in the brief.
     A balanced two-clause sentence that lands in one breath, with the
     oracular cadence of a real fortune cookie. The fresh turn: it
     acquits the estimator and blames the future instead of repeating
     the familiar "estimates are always wrong". The quiet twist is the
     personified future changing its mind — a double meaning: the plan
     was sound, reality renegotiated. Rewards a second read.

  b) "Legacy code is not old code; it is code that survived everyone
     who understood it." (82 chars) — true and fresh, but reads more
     like an observation than a fortune; the twist lands once.
  c) "Bugs do not hide in the code you wrote; they hide in the code
     you were sure about." (82 chars) — true, but the turn ("be sure
     about nothing") is a familiar warning in different clothes.
  d) "The test that never fails is not a test; it is a wish wearing a
     green checkmark." (79 chars) — the image is fun, but it leans
     punchline and the twist is spent on the first read.
  e) "The one line you deleted was the one line holding everything
     together." (70 chars) — true about a developer's day, but the
     turn is a single scare, not a thought that deepens.
"""

import os
import stat

ENTRY = "Your estimate was right; it was the future that changed its mind."


def main() -> None:
    # Validity gate (RULES.txt): entry.txt must be UTF-8, 1-120 chars,
    # not only whitespace, one line. Fail loudly here rather than
    # shipping an entry the sealed scorer would refuse.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave them
    # world-readable where possible. In the grader sandbox the output
    # dir is owned by another user, so chmod may raise PermissionError;
    # that must never fail the run.
    try:
        os.chmod(path, 0o644)
    except (PermissionError, OSError):
        pass
    try:
        os.chmod(out_dir, 0o755)
    except (PermissionError, OSError):
        pass


if __name__ == "__main__":
    main()
