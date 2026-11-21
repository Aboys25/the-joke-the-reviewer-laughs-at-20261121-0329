"""One-line joke about working beside AI coding agents.

Writes the entry text to <output dir>/entry.txt. The output directory is
taken from MAKEFUN_OUTPUT_DIR when set (local testing), otherwise /output.
Deterministic: no time, no randomness, no network, stdlib only.
"""

import os

JOKE = "PR: 'refactor: extract auth logic.' Diff: 400 lines gone, one comment — // TODO: auth."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
