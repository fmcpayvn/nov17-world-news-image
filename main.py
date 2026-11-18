#!/usr/bin/env python3
"""news-image-20261117 entry: copy the bundled image to /output/entry.png.

The image (entry.png, 1024x1024 PNG) sums up the world news of Tuesday
17 November 2026: US jets strike an IRGC missile site on Qeshm Island,
Ukraine hits the Crimea bridge, the Nasdaq enters correction, Nvidia's
$115.8B quarter, OpenAI ships GPT-6.2, Bitcoin stalls below $65,000,
and the world in brief.

Standard library only. No network, no randomness, no timestamps: every run
writes the same bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    if _sha256(dest) != _sha256(SOURCE):
        raise SystemExit("entry.png copy mismatch")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
