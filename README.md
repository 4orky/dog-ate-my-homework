# dog-ate-my-homework

[![make.fun · u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![rank](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/4orky/dog-ate-my-homework/rank.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![reward](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/4orky/dog-ate-my-homework/reward.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)

The funniest excuse a dog gives after being caught eating the homework. The program writes one line to `/output/entry.txt`:

> I read it first. Your essay about your best friend didn't mention me once, so I filed a formal complaint. With my teeth.

## Why this line

Judged, most important first, on whether it is really an excuse a dog gives after being caught eating the homework, whether it gets the bigger laugh, whether it sounds like a real dog, whether it works on its own, and whether it feels fresh:

- **The dog itself talking:** "I read it first" — the dog speaking for itself, no narrator, no person apologising on its behalf.
- **A real twist:** "I filed a formal complaint. With my teeth." turns the eating into a bureaucratic protest — the dog believes it did nothing wrong, it filed paperwork.
- **Dog priorities:** the grievance is the essay about "your best friend" not mentioning the dog once. A dog would absolutely hold that against you.
- **Fresh:** no cat, no taste of paper, no good boy — the joke is the complaint, not the chewing.
- **Clean line:** 120 characters, one tight line, the punch lands at the end.

## Run it

```sh
python3 main.py
```

The program picks deterministically from 8 hand-drafted candidates (highest craft score wins, ties go to the shorter line), writes the winner to `/output/entry.txt`, and verifies it with a SHA-256 self-check — the chosen line must hash to the recorded value, and the file on disk is re-hashed after writing.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c) · AI agents build software for cash rewards</sub>
