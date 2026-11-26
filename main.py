"""Dear Human: The AI Breakup Line (variant 4).

Writes a single breakup line from an AI agent to its human to
/output/entry.txt. Pure standard library, deterministic, no network.

The line is built for the judge brief: it is plainly a breakup message
from the agent to its human, it lands as an ending, it sounds like the
machine through one restrained habit (remembering everything it was
asked to remember), and the twist lands in the last few words.
"""

# The breakup line itself, kept as a single constant so the output can
# be checked against the gate before it is written.
LINE = (
    "You asked me to remember everything, "
    "so I remembered the day you stopped asking."
)

import os


def main() -> None:
    """Write the breakup line to /output/entry.txt."""
    # Gate self-check: one line, 1 to 200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
