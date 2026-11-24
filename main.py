# The Dog Ate My Homework: Funniest Excuse — make.fun bounty
# u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c
#
# The program writes one excuse (1-200 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. really an excuse a dog gives after being caught eating the homework,
#      in the dog's own voice
#   2. gets the bigger laugh: a twist, a piece of dog logic that lands
#      in a single line
#   3. sounds like a real dog, with a dog's priorities and none of a
#      person's embarrassment
#   4. works on its own, with no setup and nothing that needs a second
#      line to make sense
#   5. fresh: no stock lines about the cat, the taste of paper, or being
#      a good boy
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: on-subject 10, laugh 10, dog voice 10, tight 9, fresh 9 = 48
    ("I read it first. Your essay about your best friend didn't mention "
     "me once, so I filed a formal complaint. With my teeth.",
     48),
    # score: on-subject 10, laugh 9, dog voice 10, tight 9, fresh 9 = 47
    ("I didn't eat your homework. I ate the answers, and now I'm the "
     "only one in this house who knows them. Ask me anything. "
     "I won't tell.",
     47),
    # score: on-subject 10, laugh 9, dog voice 9, tight 9, fresh 9 = 46
    ("You wrote 'the dog ate my homework' in your diary as an excuse, "
     "so I made it true. You're welcome. I do my own stunts.",
     46),
    # score: on-subject 10, laugh 9, dog voice 9, tight 9, fresh 8 = 45
    ("The teacher said to hand it in. I took that literally. "
     "It is in. In me.",
     45),
    # score: on-subject 10, laugh 8, dog voice 9, tight 9, fresh 8 = 44
    ("I ate it because it was the only thing in this house that paid "
     "attention to you for more than five minutes, and I got jealous.",
     44),
    # score: on-subject 10, laugh 8, dog voice 9, tight 9, fresh 8 = 44
    ("I didn't eat it. It attacked me. It was full of words I couldn't "
     "pronounce, so I defended myself. In self-defence. With gravy.",
     44),
    # score: on-subject 10, laugh 8, dog voice 9, tight 8, fresh 8 = 43
    ("It was blank, so I filled it in. With teeth marks. "
     "That's handwriting.",
     43),
    # score: on-subject 10, laugh 8, dog voice 8, tight 9, fresh 7 = 42
    ("Homework said 'due Friday'. I heard 'do Friday'. I did Friday. "
     "The paper was dessert.",
     42),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_STOCK_MOVES = ("the cat", "tastes like paper", "taste of paper",
                      "good boy", "i'm a good boy")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_STOCK_MOVES), \
            f"candidate uses a stock move: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import hashlib
    import os
    # SHA-256 self-check: the chosen line must hash to the value recorded
    # when the candidates were drafted, so a silent edit to the winning
    # text (or to the file on disk) is caught instead of shipped.
    expected_sha256 = (
        "cd41eb27710689b8cd84ba9d7ee3784990bb8bd535af7a8d8b665ddd1e806616"
    )
    actual_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    assert actual_sha256 == expected_sha256, \
        f"chosen line hash changed: {actual_sha256}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 200, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    # Re-hash what is on disk: the file the gate reads must match the
    # chosen line byte for byte, not just in length.
    written_sha256 = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert written_sha256 == expected_sha256, \
        f"entry.txt hash changed on disk: {written_sha256}"
    print(line)


if __name__ == "__main__":
    main()
