"""Write the 21 November 2026 world news poster to /output/entry.png.

Reads the poster image bundled in this repo and copies it to the output
path the harness expects. Deterministic: same input bytes, same output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    if size > 1_048_576:
        print("entry.png is over the 1 MiB gate: %d bytes" % size, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (DST, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
