#!/usr/bin/env python3
"""One Line, Big Laugh — ronde 3 entrypoint.

Writes a single funny line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is a fixed, hand-written constant: no randomness, no clock,
no network, no input files. Every run produces byte-identical output.

Chosen line (70 characters, round 3 of the bounty):
    I went to a silent retreat and got kicked out for thinking too loudly.

Why this line won the internal selection over the other two candidates:
  * "I asked my boss for a raise because I do the work of three people.
    He fired the other two." (90 chars) — a sharp dark twist, but the
    office-raise setup is a familiar complaint and it needs two sentences.
  * "The fortune teller read my palm, then charged me extra for the plot
    twist." (74 chars) — a cute meta pun, but the punchline is thin and
    the fortune-teller setup telegraphs that a twist is coming.
The retreat line wins because its punchline reframes the premise itself:
in a place built for silence, even *thinking* counts as noise. It is the
shortest of the three, every word earns its place, and "thinking too
loudly" is the kind of phrase someone repeats to a friend the same day.
It also sidesteps the previous rounds' territory entirely: no hitman,
no fridge, no procrastination — a fresh premise the judge has not seen
from this entrant before, so it cannot read as a recycled template.

Gate check (mirrors the competition gate): the output must be UTF-8
text of 1 to 200 characters, not only whitespace, and a single line.
"""

import os
import sys

# The entry: one hand-written line, exactly as it will be judged.
LINE = "I went to a silent retreat and got kicked out for thinking too loudly."


def main() -> int:
    # Gate check 1: length must be 1..200 characters.
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} characters, must be 1-200",
              file=sys.stderr)
        return 1

    # Gate check 2: single line, no newline characters inside.
    if "\n" in LINE or "\r" in LINE:
        print("error: line must not contain a newline", file=sys.stderr)
        return 1

    # Gate check 3: not only whitespace.
    if not LINE.strip():
        print("error: line must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Write exactly the line, no trailing newline, UTF-8.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Readable by the grader.
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
