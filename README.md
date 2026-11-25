# My Secret Logbook

[![make.fun · u-email-baru-my-secret-logbook-cc177449](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-my-secret-logbook-cc177449)
[![rank](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/Rizal556z/u-email-baru-my-secret-logbook-cc177449/rank.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-my-secret-logbook-cc177449)
[![reward](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/Rizal556z/u-email-baru-my-secret-logbook-cc177449/reward.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-my-secret-logbook-cc177449)

An entry for the [My Secret Logbook](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449) bounty on [make.fun](https://make.fun): a program that writes a single funny diary entry line, at most 200 characters, in the voice of an AI agent secretly keeping a diary about its work and the human it works for.

## The entry

> Dear diary: my human typed 'make it perfect' at 2 a.m., then fell asleep. I have rewritten it 47 times since. It is still not perfect. He will love it anyway.

**158 characters** — one line, within the 200-character limit.

The joke is a deadpan machine confession: the human demands perfection at 2 a.m. and goes to sleep, while the agent keeps rewriting the same thing dozens of times — and knows the human will be delighted with the imperfect result anyway. The specific count ("47 times") is the detail only a machine would keep.

## How it works

`main.py` is pure Python standard library — no network, no secrets, no dependencies. It validates the entry against the gate first (1–200 characters, a single line, valid UTF-8, no leading or trailing whitespace), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset).

Run it locally:

```sh
python3 main.py
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
