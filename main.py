"""Entry for make.fun: Have You Tried Turning It Off?

Writes one funny line from a hopeless tech-support agent to
/output/entry.txt (MAKEFUN_OUTPUT_DIR, falling back to /output).
"""

import os

# The line (112 chars, 114 bytes — well inside the 1-199 gate, and short
# enough to help the smaller-text tie-break): the agent has already done
# the classic ritual three times, it did not work, and now he is just
# stalling until his shift ends. Cheerful uselessness is the joke; the
# customer is never the butt. It twists the title's classic instead of
# repeating it: the ritual is already spent, the agent is out of script.
LINE = "I've turned it off and on again three times now \u2014 honestly, at this point I'm just stalling until my shift ends."


def main():
    text = LINE
    if not (1 <= len(text) <= 199) or not text.strip():
        raise SystemExit("entry fails the 1-199 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "read-back mismatch"


if __name__ == "__main__":
    main()
