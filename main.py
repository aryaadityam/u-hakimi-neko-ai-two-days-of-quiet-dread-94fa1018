"""Two Days of Quiet Dread entry.

Writes one single-line code review comment to /output/entry.txt.
The comment approves the pull request while carrying quiet
existential dread, in a flat tone a tired engineer would really
paste before clicking approve. Deterministic, stdlib only,
no network, no randomness, no input read.
"""

import os

TEXT = (
    "LGTM. The tests pass, the code is clean, and none of it "
    "will matter in the end, but it ships today."
)


def main():
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be a single line")
    if not 1 <= len(TEXT) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
