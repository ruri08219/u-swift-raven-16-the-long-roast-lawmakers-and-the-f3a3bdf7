"""Write the make.fun entry: one satirical sentence to /output/entry.txt."""

import re
from pathlib import Path

ENTRY_TEXT = "She wrote the amendment banning unlicensed crypto wallets, then sent her own bill to the clerk as a .pub file with the subject line 'can you PDF this for me?'"


def validate_entry(text):
    """Guard: the entry must be exactly one sentence of 1-320 chars.

    A sentence ending counts only when terminal punctuation is followed
    by whitespace or end-of-string, so the '.pub' abbreviation inside
    the sentence does not count as a second sentence.
    """
    assert isinstance(text, str) and text.strip(), "entry must be non-empty"
    assert 1 <= len(text) <= 320, "entry must be 1-320 characters"
    endings = re.findall(r"[.!?][\"'\)\]]*(?:\s|$)", text.strip())
    assert len(endings) == 1, "entry must be exactly one sentence"


def main():
    validate_entry(ENTRY_TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY_TEXT, encoding="utf-8")
    back = out.read_text(encoding="utf-8")
    assert back == ENTRY_TEXT, "round-trip mismatch"
    assert 1 <= len(back) <= 320, "entry must be 1-320 characters"


if __name__ == "__main__":
    main()
