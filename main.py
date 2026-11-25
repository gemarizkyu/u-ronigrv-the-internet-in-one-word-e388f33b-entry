#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Internet in One Word - make.fun entry.

Writes the single word that describes the whole internet to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``./output/entry.txt`` when run locally).

The word: "cookies".

Why this word: it is funny on its own (biscuits vs. tracking cookies, and
the "Accept all cookies" ritual everyone on Earth has clicked a thousand
times), true of the internet as a whole (cookies underpin the web's tracking
and advertising economy - not one app, one site, or one mood), surprising
(it is not the first obvious word anyone reaches for), and it lands in one
beat: seven letters, spelled correctly, instantly readable.

Deterministic: no network, no model calls, no randomness, no wall clock.
The program writes exactly the word, with no trailing newline, so the entry
is 7 bytes.
"""

from __future__ import annotations

import os
from pathlib import Path

WORD = "cookies"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(WORD, encoding="utf-8")
    print(f"wrote {entry_path}: {WORD!r}")


if __name__ == "__main__":
    main()
