"""Write the make.fun entry: one satirical sentence to /output/entry.txt."""

from pathlib import Path

ENTRY = "She wrote the amendment banning unlicensed crypto wallets, then sent her own bill to the clerk as a .pub file with the subject line 'can you PDF this for me?'"

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    back = out.read_text(encoding="utf-8")
    assert back == ENTRY, "round-trip mismatch"
    assert 1 <= len(back) <= 320, "entry must be 1-320 characters"


if __name__ == "__main__":
    main()
