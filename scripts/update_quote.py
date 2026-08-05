from __future__ import annotations

from datetime import date
from pathlib import Path
import re

README = Path("README.md")
START = "<!-- DEV_QUOTE_START -->"
END = "<!-- DEV_QUOTE_END -->"

QUOTES = [
    ("Programs must be written for people to read, and only incidentally for machines to execute.", "Harold Abelson"),
    ("Simplicity is prerequisite for reliability.", "Edsger W. Dijkstra"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("The function of good software is to make the complex appear to be simple.", "Grady Booch"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
]

def main() -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise RuntimeError("README quote markers are missing.")

    quote, author = QUOTES[date.today().toordinal() % len(QUOTES)]
    replacement = f"{START}\n> “{quote}” — {author}\n{END}"

    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        replacement,
        text,
        count=1,
        flags=re.DOTALL,
    )
    README.write_text(updated, encoding="utf-8")

if __name__ == "__main__":
    main()
