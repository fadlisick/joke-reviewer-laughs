"""Write one joke about working beside AI coding agents to /output/entry.txt.

The joke is a single line, 1 to 280 characters, no trailing newline, so the
gate reads exactly the joke and nothing else. No network, no input, no
randomness: the same text every run.
"""

import os

JOKE = (
    "I told my agent the reviewer hates big diffs, so it split its "
    "5,000-line PR into 5,000 PRs, each titled 'part 1 of 1'."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"joke is {len(text)} characters, must be 1-280")
    # Never chmod the output dir itself: in the grader sandbox it is owned
    # by another user and chmod raises PermissionError. Only chmod the file
    # this program creates, which it owns. umask 022 makes the fresh file
    # 0644 on its own; the explicit chmod is a belt-and-braces for that.
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
