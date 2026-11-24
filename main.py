"""Dad Joke Showdown entry.

Writes exactly one dad joke to /output/entry.txt.
"""

from pathlib import Path

JOKE = "I brought a pencil to my job interview, just in case they asked me to draw on my experience."


def main() -> None:
    # The gate accepts 1 to 200 characters of UTF-8 text, nothing else.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
