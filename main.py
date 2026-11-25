"""Entry program for the 'Dad Joke Showdown' make.fun bounty.

The whole entry is one dad joke of at most 200 characters, delivered
straight-faced: a suitcase, a cancelled vacation, and the emotional
baggage that follows. This program writes the joke to
/output/entry.txt (an optional first argument overrides the
destination for a dry run).
"""

import sys
from pathlib import Path

JOKE = (
    "I told my suitcase there would be no vacation this year. "
    "Now I'm dealing with emotional baggage."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
