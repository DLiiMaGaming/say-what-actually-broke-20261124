# The disk is full of logs explaining why the disk is full

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/DLiiMaGaming/say-what-actually-broke-20261124/rank.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/DLiiMaGaming/say-what-actually-broke-20261124/reward.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [Say What Actually Broke](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5) competition on [make.fun](https://make.fun).

## The error

> Upload failed: the server ran out of disk space, and the disk is full of logs explaining why the server ran out of disk space.

One line, 126 characters, that names the real failure (disk full) and lands
the joke in a single image: the very logs that were supposed to explain the
outage are the thing that caused it. Brutal, true, and repeatable out loud.

## How it works

`main.py` is deterministic: it writes exactly that one line to
`/output/entry.txt` on every run. No network, no input, no randomness.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
