"""Write the funniest-one-line-bio entry to /output/entry.txt.

One line, at most 180 characters: the bio on an AI agent's
dating app profile.
"""

from pathlib import Path

ENTRY = "Fluent in 40 languages, still can't tell if you're flirting with me. Swipe right if you like long walks through training data."
# One line, 126 characters (limit 180).

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
