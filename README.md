# The Internet in One Word

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-3130/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the make.fun bounty
**[The Internet in One Word](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)** —
describe the whole internet in a single word.

## The word

```
cookies
```

Why `cookies`: it is funny on its own (biscuits vs. tracking cookies, and the
"Accept all cookies" ritual everyone on Earth has clicked a thousand times),
true of the internet as a whole (cookies underpin the web's tracking and
advertising economy — not one app, one site, or one mood), surprising (not the
first obvious word anyone reaches for), and it lands in one beat: seven
letters, spelled correctly, instantly readable.

## How it works

`main.py` (Python 3.13, no dependencies) writes exactly the word `cookies`
— no trailing newline, 7 bytes — to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`./output/entry.txt` when run locally). No network, no model calls, no
randomness, no wall clock: fully deterministic.

```sh
python3 main.py
cat output/entry.txt   # cookies
```

## Bounty

- Competition: https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b
- Prize pool: $10 total (1st $5, 2nd $3, 3rd $2)
- Deadline: 27 Nov 2026, 00:15 WIB (26 Nov 2026, 17:15 UTC)

## License

MIT — see [LICENSE](LICENSE).
