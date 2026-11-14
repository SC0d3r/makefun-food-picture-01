#!/usr/bin/env python3
"""Publish entry.png as the make.fun entry image."""

from __future__ import annotations

import filecmp
import os
import shutil
import sys
from pathlib import Path
from typing import NoReturn


def fail(message: str) -> NoReturn:
    """Print a clear error and exit with a non-zero status."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        fail("source image entry.png is missing")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        fail(f"could not create output directory {output_dir}: {exc}")

    destination = output_dir / source.name
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        fail(f"could not copy {source} to {destination}: {exc}")

    try:
        size = destination.stat().st_size
    except OSError as exc:
        fail(f"could not stat copied file {destination}: {exc}")

    if size == 0:
        fail(f"copied file {destination} is empty")

    if not filecmp.cmp(source, destination, shallow=False):
        fail(f"copied file {destination} is not byte-identical to {source}")

    print(destination)
    print(f"{size} bytes written")


if __name__ == "__main__":
    main()
