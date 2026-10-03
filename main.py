"""Mouse Accel Off — Show Enhanced Pointer Precision and turn it off or on."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='mouse_accel_off',
        description='Show Enhanced Pointer Precision and turn it off or on.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Mouse Accel Off')
    print('Raw pointer feel without the Mouse dialog.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
