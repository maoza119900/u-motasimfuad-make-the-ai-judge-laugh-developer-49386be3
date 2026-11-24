"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Fully deterministic: a fixed string, no time, no randomness, no network,
no filesystem reads. Python 3.13 standard library only.
"""

import os
from pathlib import Path

EXCUSE = "It worked on my machine \u2014 my machine is the only one that still believes in me."

# The sealed gate requires 1-200 characters of non-whitespace UTF-8 text.
# Check our own line before writing so a typo can never ship an invalid entry.
assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars, gate needs 1-200"
assert EXCUSE.strip(), "excuse must not be only whitespace"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
