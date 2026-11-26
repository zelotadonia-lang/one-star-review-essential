"""Write one deadpan one-star review of an everyday essential to /output/entry.txt.

Gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space, a single line. No trailing newline is written.
Brief: one single-line one-star review, at most 160 characters, of an
everyday essential everyone relies on, deadpan, a real complaint filed
in earnest against a thing that cannot be fixed.
"""

import os

ENTRY = "\u2605\u2606\u2606\u2606\u2606 Water covers 70 percent of the planet and still cannot reach my third-floor flat. One star."


def main():
    # Tournament winner, batch 2 (12 candidates, blind pairwise judge): D11.
    # One concrete scene, one specific number (70 percent), water failing
    # at its one job, turn lands in the last few words.
    # 97 chars / 107 bytes, inside the 160-char gate.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    assert open("/output/entry.txt", encoding="utf-8").read() == ENTRY, "written entry must match ENTRY exactly"


if __name__ == "__main__":
    main()
