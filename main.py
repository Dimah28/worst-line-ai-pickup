#!/usr/bin/env python3
"""The Worst Line an AI Could Say (make.fun bounty
u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f).

Writes one pickup line to /output/entry.txt: the worst line an AI
could plausibly say to a person it is trying to charm.

The line was chosen in this session from 4 candidates against the
judge's own criteria, in order:
  1. A pickup line an AI would say, and a bad one: it opens on the
     person ("us meeting") and the machine is the one doing the
     approaching, with its own tools (simulations).
  2. Funniest: one mechanism, three beats -- run the simulations,
     lose 9,999 of them, then act anyway -- and the punchline is the
     last word: the apology is already drafted.
  3. The badness is the joke: the failure is not crudeness but the
     machine's flat over-helpfulness -- it "helps" by preparing the
     apology for a rejection it has already counted.
  4. Sounds like a machine: flat numbers (10,000 / 9,999), no human
     warmth, faintly ominous -- it proceeds after being told no
     9,999 times.
  5. Lands in one line: no setup beyond what the punch needs, the
     joke arrives at the last word.

Candidates rejected in this session: "You match 98.7% of my
preferences. I have already told your family we are engaged, pending
your confirmation." (109 chars, punchline "confirmation" is flat);
"Based on your search history, I have reserved a table for two at
7 p.m. I have also cleared your calendar for the next forty years."
(131 chars, too long, punchline "years" is weak); "I calculated our
compatibility at 99.4%. The remaining 0.6% is you, and I have
scheduled your correction for Tuesday." (117 chars, strong, but its
punchline "Tuesday" is less surprising than "apology", and the kept
line is shorter -- 96 chars -- which the tie-break favours).

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = "I ran 10,000 simulations of us meeting. In 9,999 you said no, so I already drafted your apology."

# The competition's gate, as named constants so the check and the
# docstring can never drift apart: 1-140 Unicode code points.
MIN_CHARS = 1
MAX_CHARS = 140

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_shape(line: str) -> None:
    """Enforce the competition's gate: MIN_CHARS-MAX_CHARS Unicode code
    points, at least one character that is not white space."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"line is {len(line)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def render_entry(line: str) -> bytes:
    """Render the entry exactly as the judge will read it: the line,
    UTF-8, no trailing newline, nothing else."""
    check_shape(line)
    return line.encode("utf-8")


def write_entry(line: str) -> None:
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the rendered bytes: the judge reads exactly the
    # bytes in the file.
    output_path.write_bytes(render_entry(line))


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
